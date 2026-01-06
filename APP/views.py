ï»¿from django.shortcuts import render, redirect, get_object_or_404
from django.forms import formset_factory
from django.db import transaction
from datetime import date, timedelta
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse, Http404
from django.core.exceptions import PermissionDenied

from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q # Importa o Q para buscas complexas (OU)
from django.contrib.auth.models import User


# Importe os models
from .models import (
    PGR, RegraEmbarque, Veiculo, GerenciadoraRisco, Checklist, Rotograma, 
    CondutorBlacklist, # Adicionado
    Tarefa, HistoricoTarefa, SecurityTarefa, SecurityHistoricoTarefa,
    Seguro, Sinistro, VeiculoAssegurado,
    CertificadoQSMS,
    AgendaQSMS,
    QsmsTarefa, QsmsHistoricoTarefa,
    ArquivoDiverso, CertificadoFarmaco,
    AgendaFarmaco,
    FarmacoTarefa, FarmacoHistoricoTarefa
)

# Importe os forms
from .forms import (
    PGRForm, RegraEmbarqueForm, GerenciadoraRiscoForm, VeiculoForm, ChecklistForm, 
    RotogramaForm, 
    CondutorBlacklistForm, # Adicionado
    TarefaForm, HistoricoTarefaForm, SecurityTarefaForm, SecurityHistoricoTarefaForm,
    SeguroForm, SinistroForm,
    VeiculoAsseguradoForm,
    CustomAuthenticationForm, AdminUserCreationForm, CustomPasswordChangeForm,
    CertificadoQSMSForm,
    AgendaQSMSForm,
    QsmsTarefaForm, QsmsHistoricoTarefaForm,
    ArquivoDiversoForm, CertificadoFarmacoForm,
    AgendaFarmacoForm,
    FarmacoTarefaForm, FarmacoHistoricoTarefaForm,
    UserPermissionsForm, # Adicionado
)

# ===================================================================
#    A view home NÃO precisa de login, mas as outras sim.
# ===================================================================
def home_view(request):
    return render(request, 'APP/home.html')

RegraEmbarqueFormSet = formset_factory(RegraEmbarqueForm, extra=1)

@login_required
@permission_required('APP.view_gr_module', raise_exception=True)
def pgr_list_view(request):
    if request.method == 'POST':
        pgr_form = PGRForm(request.POST, request.FILES)
        regra_formset = RegraEmbarqueFormSet(request.POST, prefix='regras')
        if pgr_form.is_valid() and regra_formset.is_valid():
            with transaction.atomic():
                novo_pgr = pgr_form.save(commit=False)
                if request.user.is_authenticated: novo_pgr.responsavel_cadastro = request.user
                novo_pgr.save()
                for form_regra in regra_formset:
                    if form_regra.has_changed() and form_regra.is_valid():
                        regra_data = form_regra.cleaned_data
                        if regra_data.get('titulo'):
                            regra = RegraEmbarque.objects.create(titulo=regra_data['titulo'], descricao=regra_data.get('descricao', ''))
                            novo_pgr.regras_embarque.add(regra)
            return redirect('pgr_list')
    pgr_form = PGRForm()
    regra_formset = RegraEmbarqueFormSet(prefix='regras')
    pgrs = PGR.objects.all().prefetch_related('regras_embarque').order_by('validade')
    today = date.today()
    for pgr in pgrs:
        dias_restantes = (pgr.validade - today).days
        if dias_restantes <= 30: pgr.bg_color = 'list-group-item-danger'
        elif 31 <= dias_restantes <= 89: pgr.bg_color = 'list-group-item-warning'
        else: pgr.bg_color = 'list-group-item-success'
    context = {'pgrs': pgrs, 'pgr_form': pgr_form, 'regra_formset': regra_formset}
    return render(request, 'APP/pgr_list.html', context)

@login_required
@permission_required('APP.change_pgr', raise_exception=True)
@transaction.atomic
def pgr_update_view(request, pk):
    pgr = get_object_or_404(PGR, pk=pk)
    if request.method == 'POST':
        pgr_form = PGRForm(request.POST, request.FILES, instance=pgr)
        regra_formset = RegraEmbarqueFormSet(request.POST, prefix='regras')
        if pgr_form.is_valid() and regra_formset.is_valid():
            pgr_editado = pgr_form.save()
            pgr_editado.regras_embarque.clear()
            for form_regra in regra_formset:
                if form_regra.has_changed() and form_regra.is_valid():
                    regra_data = form_regra.cleaned_data
                    if regra_data.get('titulo'):
                        regra = RegraEmbarque.objects.create(titulo=regra_data['titulo'], descricao=regra_data.get('descricao', ''))
                        pgr_editado.regras_embarque.add(regra)
            return redirect('pgr_list')
    return redirect('pgr_list')

@login_required
@permission_required('APP.change_pgr', raise_exception=True)
def pgr_edit_form_view(request, pk):
    pgr = get_object_or_404(PGR, pk=pk)
    pgr_form = PGRForm(instance=pgr)
    initial_regras = [{'titulo': r.titulo, 'descricao': r.descricao} for r in pgr.regras_embarque.all()]
    regra_formset = RegraEmbarqueFormSet(initial=initial_regras, prefix='regras')
    context = {'pgr': pgr, 'pgr_form': pgr_form, 'regra_formset': regra_formset}
    return render(request, 'APP/partials/pgr_edit_form.html', context)

@login_required
@permission_required('APP.view_gr_module', raise_exception=True)
def checklist_view(request):
    gerenciadoras = GerenciadoraRisco.objects.all().order_by('nome')
    veiculos = Veiculo.objects.all()
    veiculos_cavalos = veiculos.filter(tipo='Cavalo Mecanico').order_by('placa')
    veiculos_carretas = veiculos.filter(tipo='Carreta').order_by('placa')
    checklists_map = {(c.veiculo_id, c.gerenciadora_id): c for c in Checklist.objects.select_related('ultimo_usuario', 'gerenciadora').all()}
    today = date.today()
    def get_status_data(veiculo, gr):
        checklist = checklists_map.get((veiculo.id, gr.id))
        if not checklist:
            return {'checklist': None, 'bg_color': 'table-light', 'display_text': '--', 'display_class': 'text-muted'}
        if checklist.aprovado == 'Nao':
            return {'checklist': checklist, 'bg_color': 'table-light', 'display_text': 'Reprovado', 'display_class': 'text-danger fw-bold'}
        validade_final = None
        if checklist.data_fim_validade:
            validade_final = checklist.data_fim_validade
        elif checklist.data_aprovacao:
            validade_final = checklist.data_aprovacao + timedelta(days=gr.validade_checklist)
        if validade_final:
            dias_restantes = (validade_final - today).days
            if dias_restantes <= 0:
                bg_color, display_text, display_class = 'table-danger', 'Vencido', 'fw-bold'
            elif dias_restantes <= 10:
                bg_color, display_text, display_class = 'table-danger', f'{dias_restantes} dias', ''
            elif 11 <= dias_restantes <= 15:
                bg_color, display_text, display_class = 'table-warning', f'{dias_restantes} dias', ''
            else:
                bg_color, display_text, display_class = 'table-success', f'{dias_restantes} dias', ''
            return {'checklist': checklist, 'bg_color': bg_color, 'display_text': display_text, 'display_class': display_class, 'validade': validade_final}
        return {'checklist': checklist, 'bg_color': 'table-success', 'display_text': 'Aprovado', 'display_class': '', 'validade': None}
    grades = [
        {'titulo': 'Cavalos Mecanicos', 'dados': [{'veiculo': v, 'status_list': [{'gr': gr, 'status': get_status_data(v, gr)} for gr in gerenciadoras]} for v in veiculos_cavalos]},
        {'titulo': 'Carretas', 'dados': [{'veiculo': v, 'status_list': [{'gr': gr, 'status': get_status_data(v, gr)} for gr in gerenciadoras]} for v in veiculos_carretas]},
    ]
    context = {
        'gerenciadoras': gerenciadoras,
        'veiculos': veiculos,
        'form_gr': GerenciadoraRiscoForm(),
        'form_veiculo': VeiculoForm(),
        'form_checklist': ChecklistForm(),
        'grades': grades,
    }
    return render(request, 'APP/checklist_view.html', context)

@login_required
@permission_required('APP.add_checklist', raise_exception=True)
def gerenciadora_create_view(request):
    if request.method == 'POST':
        form = GerenciadoraRiscoForm(request.POST)
        if form.is_valid(): form.save()
    return redirect('checklist_view')

@login_required
@permission_required('APP.change_checklist', raise_exception=True)
def gerenciadora_update_view(request, pk):
    gerenciadora = get_object_or_404(GerenciadoraRisco, pk=pk)
    if request.method == 'POST':
        form = GerenciadoraRiscoForm(request.POST, instance=gerenciadora)
        if form.is_valid(): form.save()
    return redirect('checklist_view')

@login_required
@permission_required('APP.delete_checklist', raise_exception=True)
def gerenciadora_delete_view(request, pk):
    gerenciadora = get_object_or_404(GerenciadoraRisco, pk=pk)
    if request.method == 'POST': gerenciadora.delete()
    return redirect('checklist_view')

@login_required
@permission_required('APP.add_checklist', raise_exception=True)
def veiculo_create_view(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid(): form.save()
    return redirect('checklist_view')

@login_required
@permission_required('APP.change_checklist', raise_exception=True)
def veiculo_update_view(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    if request.method == 'POST':
        form = VeiculoForm(request.POST, instance=veiculo)
        if form.is_valid(): form.save()
    return redirect('checklist_view')

@login_required
@permission_required('APP.delete_checklist', raise_exception=True)
def veiculo_delete_view(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    if request.method == 'POST': veiculo.delete()
    return redirect('checklist_view')

@login_required
@permission_required('APP.add_checklist', raise_exception=True)
def checklist_create_or_update_view(request, pk=None):
    instance = get_object_or_404(Checklist, pk=pk) if pk else None
    if request.method == 'POST':
        form = ChecklistForm(request.POST, instance=instance)
        if form.is_valid():
            checklist = form.save(commit=False)
            if request.user.is_authenticated:
                checklist.ultimo_usuario = request.user
            if form.cleaned_data.get('data_aprovacao') and form.cleaned_data.get('data_fim_validade'):
                checklist.data_aprovacao = None 
            checklist.save()
            return redirect('checklist_view')
    return redirect('checklist_view')

@login_required
@permission_required('APP.view_gr_module', raise_exception=True)
def rotograma_list_view(request):
    rotogramas = Rotograma.objects.all().order_by('nome_titulo')
    form = RotogramaForm()
    context = {'rotogramas': rotogramas, 'form': form}
    return render(request, 'APP/rotograma_list.html', context)

@login_required
@permission_required('APP.add_rotograma', raise_exception=True)
def rotograma_create_view(request):
    if request.method == 'POST':
        form = RotogramaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('rotograma_list')

@login_required
@permission_required('APP.change_rotograma', raise_exception=True)
def rotograma_update_view(request, pk):
    rotograma = get_object_or_404(Rotograma, pk=pk)
    if request.method == 'POST':
        form = RotogramaForm(request.POST, request.FILES, instance=rotograma)
        if form.is_valid():
            form.save()
    return redirect('rotograma_list')

@login_required
@permission_required('APP.delete_rotograma', raise_exception=True)
def rotograma_delete_view(request, pk):
    rotograma = get_object_or_404(Rotograma, pk=pk)
    if request.method == 'POST':
        rotograma.delete()
    return redirect('rotograma_list')

# --- VIEWS DE TAREFAS DE GR (EXISTENTES E CORRIGIDAS) ---
@login_required
@permission_required('APP.view_gr_module', raise_exception=True)
def tarefa_kanban_view(request):
    try:
        limite_finalizadas = int(request.GET.get('limite_finalizadas', 10))
    except ValueError:
        limite_finalizadas = 10
    
    tarefas_pendentes = Tarefa.objects.filter(status='Pendente')
    tarefas_iniciadas = Tarefa.objects.filter(status='Iniciada')
    tarefas_finalizadas = Tarefa.objects.filter(status='Finalizada')[:limite_finalizadas]
    
    context = {
        'tarefas_pendentes': tarefas_pendentes,
        'tarefas_iniciadas': tarefas_iniciadas,
        'tarefas_finalizadas': tarefas_finalizadas,
        'form_tarefa': TarefaForm(),
        'form_acao': HistoricoTarefaForm(),
        'limite_finalizadas': limite_finalizadas + 10,
        'titulo_pagina': 'GR - Tarefas',
    }
    return render(request, 'APP/tarefa_kanban.html', context)

@login_required
@permission_required('APP.add_tarefa', raise_exception=True)
@require_POST
def tarefa_create_view(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST, request.FILES)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.autor = request.user
            tarefa.status = 'Pendente'
            tarefa.save()
            HistoricoTarefa.objects.create(
                tarefa=tarefa,
                usuario=request.user,
                acao="Tarefa criada."
            )
    return redirect('tarefa_list')

@login_required
@permission_required('APP.change_tarefa', raise_exception=True)
@require_POST
def tarefa_iniciar_view(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if tarefa.status == 'Pendente':
        tarefa.status = 'Iniciada'
        tarefa.save()
        HistoricoTarefa.objects.create(
            tarefa=tarefa,
            usuario=request.user,
            acao=f"Tarefa movida para 'Iniciada'."
        )
    return redirect('tarefa_list')

@login_required
@permission_required('APP.change_tarefa', raise_exception=True)
@require_POST
def tarefa_finalizar_view(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if tarefa.status == 'Iniciada':
        tarefa.status = 'Finalizada'
        tarefa.save()
        HistoricoTarefa.objects.create(
            tarefa=tarefa,
            usuario=request.user,
            acao=f"Tarefa movida para 'Finalizada'."
        )
    return redirect('tarefa_list')

@login_required
@permission_required('APP.view_gr_module', raise_exception=True)
def tarefa_detalhes_json(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    historico = tarefa.historico.all().values('timestamp', 'acao', 'usuario__username')
    historico_list = [
        f"{item['timestamp'].strftime('%d/%m/%Y %H:%M')} ({item['usuario__username']}): {item['acao']}" 
        for item in historico
    ]
    data = {
        'id': tarefa.id, 'titulo': tarefa.titulo, 'descricao': tarefa.descricao,
        'status': tarefa.status, 'historico': historico_list,
    }
    return JsonResponse(data)

@login_required
@permission_required('APP.change_tarefa', raise_exception=True)
@require_POST
def tarefa_adicionar_acao_view(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    form = HistoricoTarefaForm(request.POST, request.FILES)
    if form.is_valid():
        acao = form.save(commit=False)
        acao.tarefa = tarefa
        acao.usuario = request.user
        acao.save()
    return redirect('tarefa_list')

# --- NOVAS VIEWS PARA TAREFAS DE SECURITY (INDEPENDENTES) ---
@login_required
@permission_required('APP.view_security_module', raise_exception=True)
def security_tarefa_kanban_view(request):
    try:
        limite_finalizadas = int(request.GET.get('limite_finalizadas', 10))
    except ValueError:
        limite_finalizadas = 10
    
    tarefas_pendentes = SecurityTarefa.objects.filter(status='Pendente')
    tarefas_iniciadas = SecurityTarefa.objects.filter(status='Iniciada')
    tarefas_finalizadas = SecurityTarefa.objects.filter(status='Finalizada')[:limite_finalizadas]
    
    context = {
        'tarefas_pendentes': tarefas_pendentes,
        'tarefas_iniciadas': tarefas_iniciadas,
        'tarefas_finalizadas': tarefas_finalizadas,
        'form_tarefa': SecurityTarefaForm(),
        'form_acao': SecurityHistoricoTarefaForm(),
        'limite_finalizadas': limite_finalizadas + 10,
        'titulo_pagina': 'Security - Tarefas',
    }
    return render(request, 'APP/tarefa_kanban_security.html', context)

@login_required
@permission_required('APP.add_securitytarefa', raise_exception=True)
@require_POST
def security_tarefa_create_view(request):
    if request.method == 'POST':
        form = SecurityTarefaForm(request.POST, request.FILES)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.autor = request.user
            tarefa.status = 'Pendente'
            tarefa.save()
            SecurityHistoricoTarefa.objects.create(
                tarefa=tarefa,
                usuario=request.user,
                acao="Tarefa criada."
            )
    return redirect('security_tarefa_list')

@login_required
@permission_required('APP.change_securitytarefa', raise_exception=True)
@require_POST
def security_tarefa_iniciar_view(request, pk):
    tarefa = get_object_or_404(SecurityTarefa, pk=pk)
    if tarefa.status == 'Pendente':
        tarefa.status = 'Iniciada'
        tarefa.save()
        SecurityHistoricoTarefa.objects.create(
            tarefa=tarefa,
            usuario=request.user,
            acao=f"Tarefa movida para 'Iniciada'."
        )
    return redirect('security_tarefa_list')

@login_required
@permission_required('APP.change_securitytarefa', raise_exception=True)
@require_POST
def security_tarefa_finalizar_view(request, pk):
    tarefa = get_object_or_404(SecurityTarefa, pk=pk)
    if tarefa.status == 'Iniciada':
        tarefa.status = 'Finalizada'
        tarefa.save()
        SecurityHistoricoTarefa.objects.create(
            tarefa=tarefa,
            usuario=request.user,
            acao=f"Tarefa movida para 'Finalizada'."
        )
    return redirect('security_tarefa_list')

@login_required
@permission_required('APP.view_security_module', raise_exception=True)
def security_tarefa_detalhes_json(request, pk):
    tarefa = get_object_or_404(SecurityTarefa, pk=pk)
    historico = tarefa.historico.all().values('timestamp', 'acao', 'usuario__username')
    historico_list = [
        f"{item['timestamp'].strftime('%d/%m/%Y %H:%M')} ({item['usuario__username']}): {item['acao']}" 
        for item in historico
    ]
    data = {
        'id': tarefa.id, 'titulo': tarefa.titulo, 'descricao': tarefa.descricao,
        'status': tarefa.status, 'historico': historico_list,
    }
    return JsonResponse(data)

@login_required
@permission_required('APP.change_securitytarefa', raise_exception=True)
@require_POST
def security_tarefa_adicionar_acao_view(request, pk):
    tarefa = get_object_or_404(SecurityTarefa, pk=pk)
    form = SecurityHistoricoTarefaForm(request.POST, request.FILES)
    if form.is_valid():
        acao = form.save(commit=False)
        acao.tarefa = tarefa
        acao.usuario = request.user
        acao.save()
    return redirect('security_tarefa_list')

# --- VIEWS DE SEGUROS, SINISTROS E VEÃCULOS ASSEGURADOS (COM @login_required) ---

@login_required
@permission_required('APP.view_security_module', raise_exception=True)
def seguro_list_view(request):
    if request.method == 'POST':
        form = SeguroForm(request.POST, request.FILES)
        if form.is_valid():
            seguro = form.save(commit=False)
            if request.user.is_authenticated:
                seguro.responsavel_cadastro = request.user
            seguro.save()
            return redirect('seguro_list')
    seguros = Seguro.objects.all().order_by('vigencia')
    today = date.today()
    for seguro in seguros:
        dias_restantes = (seguro.vigencia - today).days
        if dias_restantes <= 30:
            seguro.bg_color = 'list-group-item-danger'
        elif 31 <= dias_restantes <= 89:
            seguro.bg_color = 'list-group-item-warning'
        else:
            seguro.bg_color = 'list-group-item-success'
    context = {
        'seguros': seguros,
        'seguro_form': SeguroForm(),
    }
    return render(request, 'APP/seguro_list.html', context)
@login_required
@permission_required('APP.change_seguro', raise_exception=True)
@require_POST
def seguro_update_view(request, pk):
    seguro = get_object_or_404(Seguro, pk=pk)
    form = SeguroForm(request.POST, request.FILES, instance=seguro)
    if form.is_valid():
        form.save()
    return redirect('seguro_list')

@login_required
@permission_required('APP.change_seguro', raise_exception=True)
def seguro_edit_form_view(request, pk):
    seguro = get_object_or_404(Seguro, pk=pk)
    seguro_form = SeguroForm(instance=seguro)
    context = {
        'seguro': seguro,
        'seguro_form': seguro_form,
    }
    return render(request, 'APP/partials/seguro_edit_form.html', context)

@login_required
@permission_required('APP.delete_seguro', raise_exception=True)
@require_POST
def seguro_delete_view(request, pk):
    seguro = get_object_or_404(Seguro, pk=pk)
    seguro.delete()
    return redirect('seguro_list')

@login_required
@permission_required('APP.view_security_module', raise_exception=True)
def sinistro_list_view(request):
    if request.method == 'POST':
        form = SinistroForm(request.POST, request.FILES)
        if form.is_valid():
            sinistro = form.save(commit=False)
            if request.user.is_authenticated:
                sinistro.responsavel_cadastro = request.user
            sinistro.save()
            return redirect('sinistro_list')
    sinistros = Sinistro.objects.all().order_by('-data_sinistro')
    for s in sinistros:
        if s.status == 'Em andamento':
            s.bg_color = 'list-group-item-danger'
        else:
            s.bg_color = 'list-group-item-success'
    context = {
        'sinistros': sinistros,
        'sinistro_form': SinistroForm(),
    }
    return render(request, 'APP/sinistro_list.html', context)

@login_required
@permission_required('APP.change_sinistro', raise_exception=True)
@require_POST
def sinistro_update_view(request, pk):
    sinistro = get_object_or_404(Sinistro, pk=pk)
    form = SinistroForm(request.POST, request.FILES, instance=sinistro)
    form.fields['data_sinistro'].disabled = True
    form.fields['hora_sinistro'].disabled = True
    if form.is_valid():
        form.save()
        messages.success(request, 'Sinistro atualizado com sucesso!')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f'{field}: {error}')
    return redirect('sinistro_list')

@login_required
@permission_required('APP.change_sinistro', raise_exception=True)
def sinistro_edit_form_view(request, pk):
    sinistro = get_object_or_404(Sinistro, pk=pk)
    sinistro_form = SinistroForm(instance=sinistro)
    sinistro_form.fields['data_sinistro'].widget.attrs['readonly'] = True
    sinistro_form.fields['hora_sinistro'].widget.attrs['readonly'] = True
    context = {
        'sinistro': sinistro,
        'sinistro_form': sinistro_form,
    }
    return render(request, 'APP/partials/sinistro_edit_form.html', context)

@login_required
@permission_required('APP.delete_sinistro', raise_exception=True)
@require_POST
def sinistro_delete_view(request, pk):
    sinistro = get_object_or_404(Sinistro, pk=pk)
    sinistro.delete()
    return redirect('sinistro_list')

@login_required
@permission_required('APP.view_security_module', raise_exception=True)
def veiculo_assegurado_list_view(request):
    if request.method == 'POST':
        form = VeiculoAsseguradoForm(request.POST)
        if form.is_valid():
            veiculo = form.save(commit=False)
            if request.user.is_authenticated:
                veiculo.responsavel_cadastro = request.user
            veiculo.save()
            return redirect('veiculo_assegurado_list')
    veiculos_assegurados = VeiculoAssegurado.objects.all().order_by('vigencia')
    today = date.today()
    for veiculo in veiculos_assegurados:
        dias_restantes = (veiculo.vigencia - today).days
        if dias_restantes <= 30:
            veiculo.bg_color = 'list-group-item-danger'
        elif 31 <= dias_restantes <= 89:
            veiculo.bg_color = 'list-group-item-warning'
        else:
            veiculo.bg_color = 'list-group-item-success'
    context = {
        'veiculos_assegurados': veiculos_assegurados,
        'va_form': VeiculoAsseguradoForm(),
    }
    return render(request, 'APP/veiculo_assegurado_list.html', context)

@login_required
@permission_required('APP.change_veiculoassegurado', raise_exception=True)
@require_POST
def veiculo_assegurado_update_view(request, pk):
    veiculo = get_object_or_404(VeiculoAssegurado, pk=pk)
    form = VeiculoAsseguradoForm(request.POST, instance=veiculo)
    if form.is_valid():
        form.save()
        messages.success(request, 'VeÃ­culo assegurado atualizado com sucesso!')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f'{field}: {error}')
    return redirect('veiculo_assegurado_list')

@login_required
@permission_required('APP.change_veiculoassegurado', raise_exception=True)
def veiculo_assegurado_edit_form_view(request, pk):
    veiculo = get_object_or_404(VeiculoAssegurado, pk=pk)
    va_form = VeiculoAsseguradoForm(instance=veiculo)
    context = {
        'veiculo': veiculo,
        'va_form': va_form,
    }
    return render(request, 'APP/partials/veiculo_assegurado_edit_form.html', context)

@login_required
@permission_required('APP.delete_veiculoassegurado', raise_exception=True)
@require_POST
def veiculo_assegurado_delete_view(request, pk):
    veiculo = get_object_or_404(VeiculoAssegurado, pk=pk)
    veiculo.delete()
    return redirect('veiculo_assegurado_list')


# --- VIEWS DE CERTIFICADOS QSMS ---

@login_required
@permission_required('APP.view_qsms_module', raise_exception=True)
def certificado_qsms_list_view(request):
    if request.method == 'POST':
        form = CertificadoQSMSForm(request.POST, request.FILES)
        if form.is_valid():
            certificado = form.save(commit=False)
            if request.user.is_authenticated:
                certificado.responsavel_cadastro = request.user
            certificado.save()
            return redirect('certificado_qsms_list')
    
    certificados = CertificadoQSMS.objects.all().order_by('validade')
    today = date.today()
    for cert in certificados:
        dias_restantes = (cert.validade - today).days
        if dias_restantes <= 30:
            cert.bg_color = 'list-group-item-danger'
        elif 31 <= dias_restantes <= 89:
            cert.bg_color = 'list-group-item-warning'
        else:
            cert.bg_color = 'list-group-item-success'
    
    context = {
        'certificados': certificados,
        'certificado_form': CertificadoQSMSForm(),
    }
    return render(request, 'APP/certificado_qsms_list.html', context)

@login_required
@permission_required('APP.change_certificadoqsms', raise_exception=True)
@require_POST
def certificado_qsms_update_view(request, pk):
    certificado = get_object_or_404(CertificadoQSMS, pk=pk)
    form = CertificadoQSMSForm(request.POST, request.FILES, instance=certificado)
    if form.is_valid():
        form.save()
    return redirect('certificado_qsms_list')

@login_required
@permission_required('APP.change_certificadoqsms', raise_exception=True)
def certificado_qsms_edit_form_view(request, pk):
    certificado = get_object_or_404(CertificadoQSMS, pk=pk)
    certificado_form = CertificadoQSMSForm(instance=certificado)
    context = {
        'certificado': certificado,
        'certificado_form': certificado_form,
    }
    return render(request, 'APP/partials/certificado_qsms_edit_form.html', context)

@login_required
@permission_required('APP.delete_certificadoqsms', raise_exception=True)
@require_POST
def certificado_qsms_delete_view(request, pk):
    certificado = get_object_or_404(CertificadoQSMS, pk=pk)
    certificado.delete()
    return redirect('certificado_qsms_list')

# --- VIEWS DE AGENDA QSMS ---

@login_required
@permission_required('APP.view_qsms_module', raise_exception=True)
def agenda_qsms_list_view(request):
    if request.method == 'POST':
        form = AgendaQSMSForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.responsavel_cadastro = request.user
            evento.save()
            messages.success(request, f"{evento.get_tipo_display()} salvo com sucesso!")
            return redirect('agenda_qsms_list')
    
    show_filter = request.GET.get('show', 'future')
    today = date.today()

    treinamentos_query = AgendaQSMS.objects.filter(tipo=AgendaQSMS.TipoEvento.TREINAMENTO)
    if show_filter == 'future':
        treinamentos_query = treinamentos_query.filter(data_evento__gte=today)
    
    eventos_query = AgendaQSMS.objects.filter(tipo=AgendaQSMS.TipoEvento.EVENTO)
    if show_filter == 'future':
        eventos_query = eventos_query.filter(data_evento__gte=today)
        
    treinamentos = treinamentos_query.order_by('data_evento', 'hora_evento')
    eventos = eventos_query.order_by('data_evento', 'hora_evento')
    
    context = {
        'treinamentos': treinamentos,
        'eventos': eventos,
        'agenda_form': AgendaQSMSForm(),
        'show_filter': show_filter, 
    }
    return render(request, 'APP/agenda_qsms_list.html', context)

@login_required
@permission_required('APP.change_agendaqsms', raise_exception=True)
def agenda_qsms_edit_form_view(request, pk):
    evento = get_object_or_404(AgendaQSMS, pk=pk)
    agenda_form = AgendaQSMSForm(instance=evento)
    if not (request.user == evento.responsavel_cadastro or request.user.is_staff):
        raise Http404 
        
    context = {
        'evento': evento,
        'agenda_form': agenda_form,
    }
    return render(request, 'APP/partials/agenda_qsms_edit_form.html', context)

@login_required
@permission_required('APP.change_agendaqsms', raise_exception=True)
@require_POST
def agenda_qsms_update_view(request, pk):
    evento = get_object_or_404(AgendaQSMS, pk=pk)
    if not (request.user == evento.responsavel_cadastro or request.user.is_staff):
        messages.error(request, "VocÃª nÃ£o tem permissÃ£o para editar este item.")
        return redirect('agenda_qsms_list')

    form = AgendaQSMSForm(request.POST, instance=evento)
    if form.is_valid():
        form.save()
        messages.success(request, f"{evento.get_tipo_display()} atualizado com sucesso!")
    else:
        messages.error(request, "Erro ao atualizar o evento.")
    return redirect('agenda_qsms_list')


@login_required
@permission_required('APP.delete_agendaqsms', raise_exception=True)
@require_POST
def agenda_qsms_delete_view(request, pk):
    evento = get_object_or_404(AgendaQSMS, pk=pk)
    if not (request.user == evento.responsavel_cadastro or request.user.is_staff):
        messages.error(request, "VocÃª nÃ£o tem permissÃ£o para excluir este item.")
        return redirect('agenda_qsms_list')
        
    tipo_display = evento.get_tipo_display()
    evento.delete()
    messages.success(request, f"{tipo_display} excluÃ­do com sucesso.")
    return redirect('agenda_qsms_list')


# --- VIEWS DE TAREFAS QSMS ---

@login_required
@permission_required('APP.view_qsms_module', raise_exception=True)
def qsms_tarefa_kanban_view(request):
    try:
        limite_finalizadas = int(request.GET.get('limite_finalizadas', 10))
    except ValueError:
        limite_finalizadas = 10
    
    tarefas_pendentes = QsmsTarefa.objects.filter(status='Pendente')
    tarefas_iniciadas = QsmsTarefa.objects.filter(status='Iniciada')
    tarefas_finalizadas = QsmsTarefa.objects.filter(status='Finalizada')[:limite_finalizadas]
    
    context = {
        'tarefas_pendentes': tarefas_pendentes,
        'tarefas_iniciadas': tarefas_iniciadas,
        'tarefas_finalizadas': tarefas_finalizadas,
        'form_tarefa': QsmsTarefaForm(),
        'form_acao': QsmsHistoricoTarefaForm(),
        'limite_finalizadas': limite_finalizadas + 10,
        'titulo_pagina': 'QSMS - Tarefas',
    }
    return render(request, 'APP/tarefa_kanban_qsms.html', context)

@login_required
@permission_required('APP.add_qsmstarefa', raise_exception=True)
@require_POST
def qsms_tarefa_create_view(request):
    if request.method == 'POST':
        form = QsmsTarefaForm(request.POST, request.FILES)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.autor = request.user
            tarefa.status = 'Pendente'
            tarefa.save()
            QsmsHistoricoTarefa.objects.create(
                tarefa=tarefa,
                usuario=request.user,
                acao="Tarefa criada."
            )
    return redirect('qsms_tarefa_list')

@login_required
@permission_required('APP.change_qsmstarefa', raise_exception=True)
@require_POST
def qsms_tarefa_iniciar_view(request, pk):
    tarefa = get_object_or_404(QsmsTarefa, pk=pk)
    if tarefa.status == 'Pendente':
        tarefa.status = 'Iniciada'
        tarefa.save()
        QsmsHistoricoTarefa.objects.create(
            tarefa=tarefa,
            usuario=request.user,
            acao=f"Tarefa movida para 'Iniciada'."
        )
    return redirect('qsms_tarefa_list')

@login_required
@permission_required('APP.change_qsmstarefa', raise_exception=True)
@require_POST
def qsms_tarefa_finalizar_view(request, pk):
    tarefa = get_object_or_404(QsmsTarefa, pk=pk)
    if tarefa.status == 'Iniciada':
        tarefa.status = 'Finalizada'
        tarefa.save()
        QsmsHistoricoTarefa.objects.create(
            tarefa=tarefa,
            usuario=request.user,
            acao=f"Tarefa movida para 'Finalizada'."
        )
    return redirect('qsms_tarefa_list')

@login_required
@permission_required('APP.view_qsms_module', raise_exception=True)
def qsms_tarefa_detalhes_json(request, pk):
    # ===================================================================
    #           INÃCIO DA CORREÃÃO (TYPO 40F -> 404)
    # ===================================================================
    tarefa = get_object_or_404(QsmsTarefa, pk=pk)
    # ===================================================================
    #                         FIM DA CORREÃÃO
    # ===================================================================
    historico = tarefa.historico.all().values('timestamp', 'acao', 'usuario__username')
    historico_list = [
        f"{item['timestamp'].strftime('%d/%m/%Y %H:%M')} ({item['usuario__username']}): {item['acao']}" 
        for item in historico
    ]
    data = {
        'id': tarefa.id, 'titulo': tarefa.titulo, 'descricao': tarefa.descricao,
        'status': tarefa.status, 'historico': historico_list,
    }
    return JsonResponse(data)

@login_required
@permission_required('APP.change_qsmstarefa', raise_exception=True)
@require_POST
def qsms_tarefa_adicionar_acao_view(request, pk):
    tarefa = get_object_or_404(QsmsTarefa, pk=pk)
    form = QsmsHistoricoTarefaForm(request.POST, request.FILES)
    if form.is_valid():
        acao = form.save(commit=False)
        acao.tarefa = tarefa
        acao.usuario = request.user
        acao.save()
    return redirect('qsms_tarefa_list')

# --- VIEWS DE ARQUIVOS DIVERSOS ---

@login_required
@permission_required('APP.view_arquivosdiversos_module', raise_exception=True)
def arquivo_diverso_list_view(request):
    if request.method == 'POST':
        form = ArquivoDiversoForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = form.save(commit=False)
            arquivo.responsavel_cadastro = request.user 
            arquivo.save()
            messages.success(request, "Arquivo salvo com sucesso!")
            return redirect('arquivo_diverso_list')
    
    # Se tiver permissÃ£o view_all, mostra todos os arquivos
    if request.user.has_perm('APP.view_all_arquivodiverso'):
        arquivos = ArquivoDiverso.objects.all().order_by('titulo')
    else:
        arquivos = ArquivoDiverso.objects.filter(responsavel_cadastro=request.user).order_by('titulo')
    
    context = {
        'arquivos': arquivos,
        'arquivo_form': ArquivoDiversoForm(),
    }
    return render(request, 'APP/arquivo_diverso_list.html', context)

@login_required
@permission_required('APP.view_arquivosdiversos_module', raise_exception=True)
@require_POST
def arquivo_diverso_update_view(request, pk):
    # Permite editar se for o dono OU tiver view_all
    if request.user.has_perm('APP.view_all_arquivodiverso'):
        arquivo = get_object_or_404(ArquivoDiverso, pk=pk)
    else:
        arquivo = get_object_or_404(ArquivoDiverso, pk=pk, responsavel_cadastro=request.user)
    
    form = ArquivoDiversoForm(request.POST, request.FILES, instance=arquivo)
    if form.is_valid():
        form.save()
        messages.success(request, "Arquivo atualizado com sucesso!")
    else:
        messages.error(request, "Erro ao atualizar o arquivo.")
    return redirect('arquivo_diverso_list')

@login_required
@permission_required('APP.view_arquivosdiversos_module', raise_exception=True)
def arquivo_diverso_edit_form_view(request, pk):
    if request.user.has_perm('APP.view_all_arquivodiverso'):
        arquivo = get_object_or_404(ArquivoDiverso, pk=pk)
    else:
        arquivo = get_object_or_404(ArquivoDiverso, pk=pk, responsavel_cadastro=request.user)
    
    arquivo_form = ArquivoDiversoForm(instance=arquivo)
    context = {
        'arquivo': arquivo,
        'arquivo_form': arquivo_form,
    }
    return render(request, 'APP/partials/arquivo_diverso_edit_form.html', context)

@login_required
@permission_required('APP.view_arquivosdiversos_module', raise_exception=True)
@require_POST
def arquivo_diverso_delete_view(request, pk):
    if request.user.has_perm('APP.view_all_arquivodiverso'):
        arquivo = get_object_or_404(ArquivoDiverso, pk=pk)
    else:
        arquivo = get_object_or_404(ArquivoDiverso, pk=pk, responsavel_cadastro=request.user)
    
    arquivo.delete()
    messages.success(request, "Arquivo excluÃ­do com sucesso.")
    return redirect('arquivo_diverso_list')


# --- VIEWS DE BLACKLIST ---

@login_required
@permission_required('APP.view_gr_module', raise_exception=True)
def blacklist_list_view(request):
    if request.method == 'POST':
        form = CondutorBlacklistForm(request.POST)
        if form.is_valid():
            condutor = form.save(commit=False)
            condutor.responsavel_cadastro = request.user
            condutor.save()
            messages.success(request, "Condutor adicionado Ã  Blacklist com sucesso!")
            return redirect('blacklist_list')
        else:
            messages.error(request, f"Erro ao salvar: {form.errors.as_text()}")

    # LÃ³gica de Busca
    query = request.GET.get('q')
    if query:
        condutores = CondutorBlacklist.objects.filter(
            Q(nome_completo__icontains=query) | Q(cpf__icontains=query)
        ).order_by('nome_completo')
    else:
        condutores = CondutorBlacklist.objects.all().order_by('nome_completo')
    
    context = {
        'condutores': condutores,
        'blacklist_form': CondutorBlacklistForm(),
    }
    return render(request, 'APP/blacklist_list.html', context)

@login_required
@permission_required('APP.change_condutorblacklist', raise_exception=True)
@require_POST
def blacklist_update_view(request, pk):
    condutor = get_object_or_404(CondutorBlacklist, pk=pk)
    if not (request.user == condutor.responsavel_cadastro or request.user.is_staff):
        messages.error(request, "VocÃª nÃ£o tem permissÃ£o para editar este condutor.")
        return redirect('blacklist_list')

    form = CondutorBlacklistForm(request.POST, instance=condutor)
    if form.is_valid():
        form.save()
        messages.success(request, "Condutor atualizado com sucesso!")
    else:
        messages.error(request, f"Erro ao atualizar: {form.errors.as_text()}")
    return redirect('blacklist_list')

@login_required
@permission_required('APP.change_condutorblacklist', raise_exception=True)
def blacklist_edit_form_view(request, pk):
    condutor = get_object_or_404(CondutorBlacklist, pk=pk)
    if not (request.user == condutor.responsavel_cadastro or request.user.is_staff):
        raise Http404 

    blacklist_form = CondutorBlacklistForm(instance=condutor)
    context = {
        'condutor': condutor,
        'blacklist_form': blacklist_form,
    }
    return render(request, 'APP/partials/blacklist_edit_form.html', context)

@login_required
@permission_required('APP.delete_condutorblacklist', raise_exception=True)
@require_POST
def blacklist_delete_view(request, pk):
    condutor = get_object_or_404(CondutorBlacklist, pk=pk)
    if not (request.user == condutor.responsavel_cadastro or request.user.is_staff):
        messages.error(request, "VocÃª nÃ£o tem permissÃ£o para excluir este condutor.")
        return redirect('blacklist_list')
        
    condutor.delete()
    messages.success(request, "Condutor removido da Blacklist com sucesso.")
    return redirect('blacklist_list')


# --- VIEWS DE AUTENTICAÃÃO ---

# FunÃ§Ã£o auxiliar para verificar superuser (usada em mÃºltiplas views)
def is_superuser(user):
    """Verifica se o usuÃ¡rio Ã© superuser"""
    return user.is_superuser

class CustomLoginView(LoginView):
    """View de login customizada."""
    form_class = CustomAuthenticationForm
    template_name = 'APP/login.html'
    redirect_authenticated_user = True

@login_required
def custom_logout_view(request):
    """View de logout."""
    logout(request)
    messages.success(request, 'VocÃª saiu da sua conta com sucesso.')
    return redirect('login') 

class CustomPasswordChangeView(PasswordChangeView):
    """View de alteraÃ§Ã£o de senha customizada."""
    form_class = CustomPasswordChangeForm
    template_name = 'APP/password_change.html'
    success_url = reverse_lazy('password_change_done')

@login_required
def password_change_done_view(request):
    """View de confirmaÃ§Ã£o de alteraÃ§Ã£o de senha."""
    messages.success(request, 'Sua senha foi alterada com sucesso!')
    return redirect('home')

@login_required
@permission_required('APP.view_farmaco_module', raise_exception=True)
def certificado_farmaco_list_view(request):
    if request.method == 'POST':
        form = CertificadoFarmacoForm(request.POST, request.FILES)
        if form.is_valid():
            certificado = form.save(commit=False)
            if request.user.is_authenticated:
                certificado.responsavel_cadastro = request.user
            certificado.save()
            return redirect('certificado_farmaco_list')
    
    certificados = CertificadoFarmaco.objects.all().order_by('validade')
    today = date.today()
    for cert in certificados:
        dias_restantes = (cert.validade - today).days
        if dias_restantes <= 30:
            cert.bg_color = 'list-group-item-danger'
        elif 31 <= dias_restantes <= 89:
            cert.bg_color = 'list-group-item-warning'
        else:
            cert.bg_color = 'list-group-item-success'
    
    context = {
        'certificados': certificados,
        'certificado_form': CertificadoFarmacoForm(),
    }
    return render(request, 'APP/certificado_farmaco_list.html', context)

@login_required
@permission_required('APP.change_certificadofarmaco', raise_exception=True)
@require_POST
def certificado_farmaco_update_view(request, pk):
    certificado = get_object_or_404(CertificadoFarmaco, pk=pk)
    form = CertificadoFarmacoForm(request.POST, request.FILES, instance=certificado)
    if form.is_valid():
        form.save()
    return redirect('certificado_farmaco_list')

@login_required
@permission_required('APP.change_certificadofarmaco', raise_exception=True)
def certificado_farmaco_edit_form_view(request, pk):
    certificado = get_object_or_404(CertificadoFarmaco, pk=pk)
    certificado_form = CertificadoFarmacoForm(instance=certificado)
    context = {
        'certificado': certificado,
        'certificado_form': certificado_form,
    }
    return render(request, 'APP/partials/certificado_farmaco_edit_form.html', context)

@login_required
@permission_required('APP.delete_certificadofarmaco', raise_exception=True)
@require_POST
def certificado_farmaco_delete_view(request, pk):
    certificado = get_object_or_404(CertificadoFarmaco, pk=pk)
    certificado.delete()
    return redirect('certificado_farmaco_list')

@login_required
@permission_required('APP.view_farmaco_module', raise_exception=True)
def agenda_farmaco_list_view(request):
    if request.method == 'POST':
        form = AgendaFarmacoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.responsavel_cadastro = request.user
            evento.save()
            messages.success(request, f"{evento.get_tipo_display()} salvo com sucesso!")
            return redirect('agenda_farmaco_list')
    
    show_filter = request.GET.get('show', 'future')
    today = date.today()

    treinamentos_query = AgendaFarmaco.objects.filter(tipo=AgendaFarmaco.TipoEvento.TREINAMENTO)
    if show_filter == 'future':
        treinamentos_query = treinamentos_query.filter(data_evento__gte=today)
    
    eventos_query = AgendaFarmaco.objects.filter(tipo=AgendaFarmaco.TipoEvento.EVENTO)
    if show_filter == 'future':
        eventos_query = eventos_query.filter(data_evento__gte=today)
        
    treinamentos = treinamentos_query.order_by('data_evento', 'hora_evento')
    eventos = eventos_query.order_by('data_evento', 'hora_evento')
    
    context = {
        'treinamentos': treinamentos,
        'eventos': eventos,
        'agenda_form': AgendaFarmacoForm(),
        'show_filter': show_filter, 
    }
    return render(request, 'APP/agenda_farmaco_list.html', context)

@login_required
@permission_required('APP.change_agendafarmaco', raise_exception=True)
def agenda_farmaco_edit_form_view(request, pk):
    evento = get_object_or_404(AgendaFarmaco, pk=pk)
    agenda_form = AgendaFarmacoForm(instance=evento)
    if not (request.user == evento.responsavel_cadastro or request.user.is_staff):
        raise Http404 
        
    context = {
        'evento': evento,
        'agenda_form': agenda_form,
    }
    return render(request, 'APP/partials/agenda_farmaco_edit_form.html', context)

@login_required
@permission_required('APP.change_agendafarmaco', raise_exception=True)
@require_POST
def agenda_farmaco_update_view(request, pk):
    evento = get_object_or_404(AgendaFarmaco, pk=pk)
    if not (request.user == evento.responsavel_cadastro or request.user.is_staff):
        messages.error(request, "VocÃª nÃ£o tem permissÃ£o para editar este item.")
        return redirect('agenda_farmaco_list')

    form = AgendaFarmacoForm(request.POST, instance=evento)
    if form.is_valid():
        form.save()
        messages.success(request, f"{evento.get_tipo_display()} atualizado com sucesso!")
    else:
        messages.error(request, "Erro ao atualizar o evento.")
    return redirect('agenda_farmaco_list')

@login_required
@permission_required('APP.delete_agendafarmaco', raise_exception=True)
@require_POST
def agenda_farmaco_delete_view(request, pk):
    evento = get_object_or_404(AgendaFarmaco, pk=pk)
    if not (request.user == evento.responsavel_cadastro or request.user.is_staff):
        messages.error(request, "VocÃª nÃ£o tem permissÃ£o para excluir este item.")
        return redirect('agenda_farmaco_list')
        
    tipo_display = evento.get_tipo_display()
    evento.delete()
    messages.success(request, f"{tipo_display} excluÃ­do com sucesso.")
    return redirect('agenda_farmaco_list')

@login_required
@permission_required('APP.view_farmaco_module', raise_exception=True)
def farmaco_tarefa_kanban_view(request):
    try:
        limite_finalizadas = int(request.GET.get('limite_finalizadas', 10))
    except ValueError:
        limite_finalizadas = 10
    
    tarefas_pendentes = FarmacoTarefa.objects.filter(status='Pendente')
    tarefas_iniciadas = FarmacoTarefa.objects.filter(status='Iniciada')
    tarefas_finalizadas = FarmacoTarefa.objects.filter(status='Finalizada')[:limite_finalizadas]
    
    context = {
        'tarefas_pendentes': tarefas_pendentes,
        'tarefas_iniciadas': tarefas_iniciadas,
        'tarefas_finalizadas': tarefas_finalizadas,
        'form_tarefa': FarmacoTarefaForm(),
        'form_acao': FarmacoHistoricoTarefaForm(),
        'limite_finalizadas': limite_finalizadas + 10,
        'titulo_pagina': 'FÃ¡rmaco - Tarefas',
    }
    return render(request, 'APP/tarefa_kanban_farmaco.html', context)

@login_required
@permission_required('APP.add_farmacotarefa', raise_exception=True)
@require_POST
def farmaco_tarefa_create_view(request):
    if request.method == 'POST':
        form = FarmacoTarefaForm(request.POST, request.FILES)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.autor = request.user
            tarefa.status = 'Pendente'
            tarefa.save()
            FarmacoHistoricoTarefa.objects.create(
                tarefa=tarefa,
                usuario=request.user,
                acao="Tarefa criada."
            )
    return redirect('farmaco_tarefa_list')

@login_required
@permission_required('APP.change_farmacotarefa', raise_exception=True)
@require_POST
def farmaco_tarefa_iniciar_view(request, pk):
    tarefa = get_object_or_404(FarmacoTarefa, pk=pk)
    if tarefa.status == 'Pendente':
        tarefa.status = 'Iniciada'
        tarefa.save()
        FarmacoHistoricoTarefa.objects.create(
            tarefa=tarefa,
            usuario=request.user,
            acao=f"Tarefa movida para 'Iniciada'."
        )
    return redirect('farmaco_tarefa_list')

@login_required
@permission_required('APP.change_farmacotarefa', raise_exception=True)
@require_POST
def farmaco_tarefa_finalizar_view(request, pk):
    tarefa = get_object_or_404(FarmacoTarefa, pk=pk)
    if tarefa.status == 'Iniciada':
        tarefa.status = 'Finalizada'
        tarefa.save()
        FarmacoHistoricoTarefa.objects.create(
            tarefa=tarefa,
            usuario=request.user,
            acao=f"Tarefa movida para 'Finalizada'."
        )
    return redirect('farmaco_tarefa_list')

@login_required
@permission_required('APP.view_farmaco_module', raise_exception=True)
def farmaco_tarefa_detalhes_json(request, pk):
    tarefa = get_object_or_404(FarmacoTarefa, pk=pk)
    historico = tarefa.historico.all().values('timestamp', 'acao', 'usuario__username')
    historico_list = [
        f"{item['timestamp'].strftime('%d/%m/%Y %H:%M')} ({item['usuario__username']}): {item['acao']}" 
        for item in historico
    ]
    data = {
        'id': tarefa.id, 'titulo': tarefa.titulo, 'descricao': tarefa.descricao,
        'status': tarefa.status, 'historico': historico_list,
    }
    return JsonResponse(data)

@login_required
@permission_required('APP.change_farmacotarefa', raise_exception=True)
@require_POST
def farmaco_tarefa_adicionar_acao_view(request, pk):
    tarefa = get_object_or_404(FarmacoTarefa, pk=pk)
    form = FarmacoHistoricoTarefaForm(request.POST, request.FILES)
    if form.is_valid():
        acao = form.save(commit=False)
        acao.tarefa = tarefa
        acao.usuario = request.user
        acao.save()
    return redirect('farmaco_tarefa_list')

# ===================================================================
#           VIEWS DE GERENCIAMENTO DE USUÃRIOS E PERMISSÃES
# ===================================================================

@user_passes_test(is_superuser)
def manage_users_list(request):
    """Lista todos os usuÃ¡rios do sistema"""
    users = User.objects.all().order_by('username')
    context = {'users': users}
    return render(request, 'APP/manage_users_list.html', context)

@user_passes_test(is_superuser)
def manage_user_permissions(request, user_id=None):
    """Criar ou editar usuÃ¡rio com permissÃµes"""
    if user_id:
        user = get_object_or_404(User, pk=user_id)
        form_title = f"Editar UsuÃ¡rio: {user.username}"
    else:
        user = None
        form_title = "Criar Novo UsuÃ¡rio"
    
    if request.method == 'POST':
        form = UserPermissionsForm(request.POST, instance=user)
        if form.is_valid():
            new_user = form.save()
            messages.success(request, f'UsuÃ¡rio {new_user.username} salvo com sucesso!')
            return redirect('manage_users_list')
    else:
        form = UserPermissionsForm(instance=user)
    
    context = {
        'form': form,
        'form_title': form_title,
        'editing': user_id is not None,
    }
    return render(request, 'APP/manage_user_permissions.html', context)

@user_passes_test(is_superuser)
@require_POST
def delete_user(request, user_id):
    """Excluir usuÃ¡rio"""
    user = get_object_or_404(User, pk=user_id)
    if user == request.user:
        messages.error(request, 'VocÃª nÃ£o pode excluir seu prÃ³prio usuÃ¡rio!')
    elif user.is_superuser:
        messages.error(request, 'NÃ£o Ã© possÃ­vel excluir um superusuÃ¡rio!')
    else:
        username = user.username
        user.delete()
        messages.success(request, f'UsuÃ¡rio {username} excluÃ­do com sucesso!')
    return redirect('manage_users_list')

# ===================================================================
#           VIEWS DE DOWNLOAD DE ARQUIVOS PROTEGIDOS
# ===================================================================

from django.http import FileResponse
import os
from django.conf import settings

@login_required
def serve_pgr_file(request, pk):
    """Serve arquivo PDF do PGR com permissÃ£o"""
    # Verifica permissÃ£o do mÃ³dulo OU permissÃ£o especÃ­fica de anexos
    if not (request.user.has_perm('APP.view_gr_module') or request.user.has_perm('APP.view_gr_attachments')):
        raise PermissionDenied("VocÃª nÃ£o tem permissÃ£o para visualizar este anexo")
    
    pgr = get_object_or_404(PGR, pk=pk)
    if pgr.arquivo_pdf:
        file_path = os.path.join(settings.MEDIA_ROOT, str(pgr.arquivo_pdf))
        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    raise Http404("Arquivo nÃ£o encontrado")

@login_required
def serve_rotograma_file(request, pk):
    """Serve arquivo PDF do Rotograma com permissÃ£o"""
    # Verifica permissÃ£o do mÃ³dulo OU permissÃ£o especÃ­fica de anexos
    if not (request.user.has_perm('APP.view_gr_module') or request.user.has_perm('APP.view_gr_attachments')):
        raise PermissionDenied("VocÃª nÃ£o tem permissÃ£o para visualizar este anexo")
    
    rotograma = get_object_or_404(Rotograma, pk=pk)
    if rotograma.arquivo_pdf:
        file_path = os.path.join(settings.MEDIA_ROOT, str(rotograma.arquivo_pdf))
        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    raise Http404("Arquivo nÃ£o encontrado")

@login_required
def serve_seguro_apolice_file(request, pk):
    """Serve arquivo de apÃ³lice do Seguro com permissÃ£o"""
    # Verifica permissÃ£o do mÃ³dulo OU permissÃ£o especÃ­fica de anexos
    if not (request.user.has_perm('APP.view_security_module') or request.user.has_perm('APP.view_security_attachments')):
        raise PermissionDenied("VocÃª nÃ£o tem permissÃ£o para visualizar este anexo")
    
    seguro = get_object_or_404(Seguro, pk=pk)
    if seguro.apolice_pdf:
        file_path = os.path.join(settings.MEDIA_ROOT, str(seguro.apolice_pdf))
        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    raise Http404("Arquivo nÃ£o encontrado")

@login_required
def serve_seguro_certificado_file(request, pk):
    """Serve arquivo de certificado do Seguro com permissÃ£o"""
    # Verifica permissÃ£o do mÃ³dulo OU permissÃ£o especÃ­fica de anexos
    if not (request.user.has_perm('APP.view_security_module') or request.user.has_perm('APP.view_security_attachments')):
        raise PermissionDenied("VocÃª nÃ£o tem permissÃ£o para visualizar este anexo")
    
    seguro = get_object_or_404(Seguro, pk=pk)
    if seguro.certificado_pdf:
        file_path = os.path.join(settings.MEDIA_ROOT, str(seguro.certificado_pdf))
        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    raise Http404("Arquivo nÃ£o encontrado")

@login_required
def serve_certificado_qsms_file(request, pk):
    """Serve arquivo PDF do Certificado QSMS com permissÃ£o"""
    # Verifica permissÃ£o do mÃ³dulo OU permissÃ£o especÃ­fica de anexos
    if not (request.user.has_perm('APP.view_qsms_module') or request.user.has_perm('APP.view_qsms_attachments')):
        raise PermissionDenied("VocÃª nÃ£o tem permissÃ£o para visualizar este anexo")
    
    certificado = get_object_or_404(CertificadoQSMS, pk=pk)
    if certificado.arquivo_pdf:
        file_path = os.path.join(settings.MEDIA_ROOT, str(certificado.arquivo_pdf))
        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    raise Http404("Arquivo nÃ£o encontrado")

@login_required
def serve_certificado_farmaco_file(request, pk):
    """Serve arquivo PDF do Certificado FÃ¡rmaco com permissÃ£o"""
    # Verifica permissÃ£o do mÃ³dulo OU permissÃ£o especÃ­fica de anexos
    if not (request.user.has_perm('APP.view_farmaco_module') or request.user.has_perm('APP.view_farmaco_attachments')):
        raise PermissionDenied("VocÃª nÃ£o tem permissÃ£o para visualizar este anexo")
    
    certificado = get_object_or_404(CertificadoFarmaco, pk=pk)
    if certificado.arquivo_pdf:
        file_path = os.path.join(settings.MEDIA_ROOT, str(certificado.arquivo_pdf))
        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    raise Http404("Arquivo nÃ£o encontrado")
