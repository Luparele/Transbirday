ï»¿from django import forms
from .models import (
    PGR, RegraEmbarque, Veiculo, GerenciadoraRisco, Checklist, Rotograma, 
    CondutorBlacklist, # Adicionado
    Tarefa, HistoricoTarefa, SecurityTarefa, SecurityHistoricoTarefa,
    Seguro, Sinistro, VeiculoAssegurado,
    CertificadoQSMS,
    AgendaQSMS,
    QsmsTarefa, QsmsHistoricoTarefa,
    ArquivoDiverso,
    CertificadoFarmaco,
    AgendaFarmaco,
    FarmacoTarefa, FarmacoHistoricoTarefa,
)
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType


class PGRForm(forms.ModelForm):
    class Meta:
        model = PGR
        fields = [
            'titulo_cliente', 'validade', 'gerente_conta',
            'contato_gc', 'email_gc', 'tipo_seguro', 'arquivo_pdf',
        ]
        widgets = {
            'validade': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'titulo_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'gerente_conta': forms.TextInput(attrs={'class': 'form-control'}),
            'contato_gc': forms.TextInput(attrs={'class': 'form-control'}),
            'email_gc': forms.EmailInput(attrs={'class': 'form-control'}),
            'tipo_seguro': forms.Select(attrs={'class': 'form-select'}),
            'arquivo_pdf': forms.FileInput(attrs={'class': 'form-control'}),
        }

class RegraEmbarqueForm(forms.ModelForm):
    class Meta:
        model = RegraEmbarque
        fields = ['titulo', 'descricao']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': CKEditorUploadingWidget(), 
        }

class GerenciadoraRiscoForm(forms.ModelForm):
    class Meta:
        model = GerenciadoraRisco
        fields = ['nome', 'validade_checklist']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'validade_checklist': forms.Select(attrs={'class': 'form-select'}),
        }

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['placa', 'categoria', 'tipo']
        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-transform: uppercase;'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
        }

# ===================================================================
#           INÃCIO DO NOVO FORMULÃRIO (BLACK LIST)
# ===================================================================
class CondutorBlacklistForm(forms.ModelForm):
    class Meta:
        model = CondutorBlacklist
        fields = ['nome_completo', 'cpf', 'data_pesquisa', 'motivo_reprovacao']
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control', 
                'data-mask': '000.000.000-00' # MÃ¡scara para o JavaScript
            }),
            'data_pesquisa': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'motivo_reprovacao': CKEditorUploadingWidget(),
        }
# ===================================================================
#                         FIM DAS ADIÃÃES
# ===================================================================

class ChecklistForm(forms.ModelForm):
    class Meta:
        model = Checklist
        fields = [
            'veiculo', 'gerenciadora', 'aprovado', 
            'data_aprovacao', 'data_fim_validade', 'motivo_reprovacao'
        ]
        widgets = {
            'veiculo': forms.Select(attrs={'class': 'form-select'}),
            'gerenciadora': forms.Select(attrs={'class': 'form-select'}),
            'aprovado': forms.Select(attrs={'class': 'form-select'}),
            'data_aprovacao': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'data_fim_validade': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'motivo_reprovacao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class RotogramaForm(forms.ModelForm):
    class Meta:
        model = Rotograma
        fields = ['nome_titulo', 'origem', 'destino', 'arquivo_pdf']
        widgets = {
            'nome_titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'origem': forms.TextInput(attrs={'class': 'form-control'}),
            'destino': forms.TextInput(attrs={'class': 'form-control'}),
            'arquivo_pdf': forms.FileInput(attrs={'class': 'form-control'}),
        }

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': CKEditorUploadingWidget(), 
        }

class HistoricoTarefaForm(forms.ModelForm):
    class Meta:
        model = HistoricoTarefa
        fields = ['acao']
        widgets = {
            'acao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Adicionar um novo comentÃ¡rio ou aÃ§Ã£o...'}),
        }
        labels = {
            'acao': 'Nova AÃ§Ã£o/ComentÃ¡rio'
        }

class SecurityTarefaForm(forms.ModelForm):
    class Meta:
        model = SecurityTarefa
        fields = ['titulo', 'descricao']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': CKEditorUploadingWidget(), 
        }

class SecurityHistoricoTarefaForm(forms.ModelForm):
    class Meta:
        model = SecurityHistoricoTarefa
        fields = ['acao']
        widgets = {
            'acao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Adicionar um novo comentÃ¡rio ou aÃ§Ã£o...'}),
        }
        labels = {
            'acao': 'Nova AÃ§Ã£o/ComentÃ¡rio'
        }

class SeguroForm(forms.ModelForm):
    class Meta:
        model = Seguro
        fields = [
            'seguradora', 'tipo_apolice', 'corretora', 'corretor',
            'contato_corretor', 'email_corretor', 'vigencia', 
            'descricao_resumo', 'apolice_pdf', 'certificado_pdf'
        ]
        widgets = {
            'seguradora': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_apolice': forms.TextInput(attrs={'class': 'form-control'}),
            'corretora': forms.TextInput(attrs={'class': 'form-control'}),
            'corretor': forms.TextInput(attrs={'class': 'form-control'}),
            'contato_corretor': forms.TextInput(attrs={'class': 'form-control'}),
            'email_corretor': forms.EmailInput(attrs={'class': 'form-control'}),
            'vigencia': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'descricao_resumo': CKEditorUploadingWidget(), 
            'apolice_pdf': forms.FileInput(attrs={'class': 'form-control'}),
            'certificado_pdf': forms.FileInput(attrs={'class': 'form-control'}),
        }

class SinistroForm(forms.ModelForm):
    class Meta:
        model = Sinistro
        fields = ['data_sinistro', 'hora_sinistro', 'seguradora_responsavel', 'status', 'detalhes']
        widgets = {
            'data_sinistro': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora_sinistro': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'seguradora_responsavel': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'detalhes': CKEditorUploadingWidget(), 
        }

class VeiculoAsseguradoForm(forms.ModelForm):
    class Meta:
        model = VeiculoAssegurado
        exclude = ['responsavel_cadastro']
        widgets = {
            'seguradora': forms.TextInput(attrs={'class': 'form-control'}),
            'vigencia': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'placa': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-transform: uppercase;'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'ano_fabricacao': forms.NumberInput(attrs={'class': 'form-control'}),
            'ano_modelo': forms.NumberInput(attrs={'class': 'form-control'}),
            'cobertura': forms.Select(attrs={'class': 'form-select'}),
            'valor_fipe_percent': forms.NumberInput(attrs={'class': 'form-control'}),
            'franquia': forms.NumberInput(attrs={'class': 'form-control'}),
            'danos_materiais': forms.NumberInput(attrs={'class': 'form-control'}),
            'danos_corporais': forms.NumberInput(attrs={'class': 'form-control'}),
            'danos_morais': forms.NumberInput(attrs={'class': 'form-control'}),
            'app_morte': forms.NumberInput(attrs={'class': 'form-control'}),
            'app_invalidez': forms.NumberInput(attrs={'class': 'form-control'}),
            'assistencia_km': forms.NumberInput(attrs={'class': 'form-control'}),
            'carro_reserva_dias': forms.NumberInput(attrs={'class': 'form-control'}),
            'cobertura_vidros': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class CertificadoQSMSForm(forms.ModelForm):
    class Meta:
        model = CertificadoQSMS
        fields = [
            'certificado', 'orgao_competente', 'link_orgao',
            'validade', 'arquivo_pdf', 'descricao'
        ]
        widgets = {
            'certificado': forms.TextInput(attrs={'class': 'form-control'}),
            'orgao_competente': forms.TextInput(attrs={'class': 'form-control'}),
            'link_orgao': forms.URLInput(attrs={'class': 'form-control'}),
            'validade': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'arquivo_pdf': forms.FileInput(attrs={'class': 'form-control'}),
            'descricao': CKEditorUploadingWidget(),
        }

class AgendaQSMSForm(forms.ModelForm):
    class Meta:
        model = AgendaQSMS
        fields = ['tipo', 'assunto', 'data_evento', 'hora_evento', 'detalhes']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-select'}), 
            'assunto': forms.TextInput(attrs={'class': 'form-control'}),
            'data_evento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora_evento': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'detalhes': CKEditorUploadingWidget(),
        }

class QsmsTarefaForm(forms.ModelForm):
    class Meta:
        model = QsmsTarefa
        fields = ['titulo', 'descricao']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': CKEditorUploadingWidget(),
        }

class QsmsHistoricoTarefaForm(forms.ModelForm):
    class Meta:
        model = QsmsHistoricoTarefa
        fields = ['acao']
        widgets = {
            'acao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Adicionar um novo comentÃ¡rio ou aÃ§Ã£o...'}),
        }
        labels = {
            'acao': 'Nova AÃ§Ã£o/ComentÃ¡rio'
        }

class ArquivoDiversoForm(forms.ModelForm):
    class Meta:
        model = ArquivoDiverso
        fields = ['titulo', 'descricao', 'arquivo_pdf']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': CKEditorUploadingWidget(),
            'arquivo_pdf': forms.FileInput(attrs={'class': 'form-control'}),
        }


# ===================================================================
#           FORMULÃRIOS DE AUTENTICAÃÃO
# ===================================================================

class CustomAuthenticationForm(AuthenticationForm):
    """FormulÃ¡rio de login customizado para Bootstrap."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'UsuÃ¡rio'
        })
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Senha'
        })

# ===================================================================
#           FORMULÃRIO DE CRIAÃÃO DE USUÃRIO (ADMIN)
# ===================================================================
class AdminUserCreationForm(forms.ModelForm):
    """FormulÃ¡rio para admin criar novos usuÃ¡rios com senha padrÃ£o."""
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff', 'is_superuser']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_staff'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['is_superuser'].widget.attrs.update({'class': 'form-check-input'})

class CustomPasswordChangeForm(PasswordChangeForm):
    """FormulÃ¡rio de alteraÃ§Ã£o de senha customizado para Bootstrap."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['new_password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['new_password2'].widget = forms.PasswordInput(attrs={'class': 'form-control'})

# ===================================================================
#           FORMULÃRIOS DE FÃRMACO
# ===================================================================

class CertificadoFarmacoForm(forms.ModelForm):
    class Meta:
        model = CertificadoFarmaco
        fields = [
            'certificado', 'orgao_competente', 'link_orgao',
            'validade', 'arquivo_pdf', 'descricao'
        ]
        widgets = {
            'certificado': forms.TextInput(attrs={'class': 'form-control'}),
            'orgao_competente': forms.TextInput(attrs={'class': 'form-control'}),
            'link_orgao': forms.URLInput(attrs={'class': 'form-control'}),
            'validade': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'arquivo_pdf': forms.FileInput(attrs={'class': 'form-control'}),
            'descricao': CKEditorUploadingWidget(),
        }

class AgendaFarmacoForm(forms.ModelForm):
    class Meta:
        model = AgendaFarmaco
        fields = ['tipo', 'assunto', 'data_evento', 'hora_evento', 'detalhes']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-select'}), 
            'assunto': forms.TextInput(attrs={'class': 'form-control'}),
            'data_evento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora_evento': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'detalhes': CKEditorUploadingWidget(),
        }

class FarmacoTarefaForm(forms.ModelForm):
    class Meta:
        model = FarmacoTarefa
        fields = ['titulo', 'descricao']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': CKEditorUploadingWidget(),
        }

class FarmacoHistoricoTarefaForm(forms.ModelForm):
    class Meta:
        model = FarmacoHistoricoTarefa
        fields = ['acao']
        widgets = {
            'acao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Adicionar um novo comentÃ¡rio ou aÃ§Ã£o...'}),
        }
        labels = {
            'acao': 'Nova AÃ§Ã£o/ComentÃ¡rio'
        }

# ===================================================================
#           FORMULÃRIO DE GERENCIAMENTO DE PERMISSÃES
# ===================================================================

class UserPermissionsForm(forms.ModelForm):
    """FormulÃ¡rio para gerenciar usuÃ¡rio e permissÃµes"""
    
    # InformaÃ§Ãµes bÃ¡sicas
    password1 = forms.CharField(
        label='Senha', 
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False,
        help_text='Deixe em branco para manter a senha atual (ao editar) ou usar a senha padrÃ£o (ao criar)'
    )
    password2 = forms.CharField(
        label='Confirmar Senha', 
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False
    )
    
    # GERENCIAMENTO DE RISCO
    view_gr_module = forms.BooleanField(required=False, label="Visualizar mÃ³dulo")
    view_gr_attachments = forms.BooleanField(required=False, label="Visualizar anexos")
    add_pgr = forms.BooleanField(required=False, label="Adicionar")
    change_pgr = forms.BooleanField(required=False, label="Editar")
    delete_pgr = forms.BooleanField(required=False, label="Excluir")
    
    add_checklist = forms.BooleanField(required=False, label="Adicionar")
    change_checklist = forms.BooleanField(required=False, label="Editar")
    delete_checklist = forms.BooleanField(required=False, label="Excluir")
    
    add_gerenciadorarisco = forms.BooleanField(required=False, label="Adicionar")
    change_gerenciadorarisco = forms.BooleanField(required=False, label="Editar")
    delete_gerenciadorarisco = forms.BooleanField(required=False, label="Excluir")
    
    add_veiculo = forms.BooleanField(required=False, label="Adicionar")
    change_veiculo = forms.BooleanField(required=False, label="Editar")
    delete_veiculo = forms.BooleanField(required=False, label="Excluir")
    
    add_rotograma = forms.BooleanField(required=False, label="Adicionar")
    change_rotograma = forms.BooleanField(required=False, label="Editar")
    delete_rotograma = forms.BooleanField(required=False, label="Excluir")
    
    add_tarefa = forms.BooleanField(required=False, label="Adicionar")
    change_tarefa = forms.BooleanField(required=False, label="Editar")
    delete_tarefa = forms.BooleanField(required=False, label="Excluir")
    
    add_condutorblacklist = forms.BooleanField(required=False, label="Adicionar")
    change_condutorblacklist = forms.BooleanField(required=False, label="Editar")
    delete_condutorblacklist = forms.BooleanField(required=False, label="Excluir")
    
    # SECURITY
    view_security_module = forms.BooleanField(required=False, label="Visualizar mÃ³dulo")
    view_security_attachments = forms.BooleanField(required=False, label="Visualizar anexos")
    add_seguro = forms.BooleanField(required=False, label="Adicionar")
    change_seguro = forms.BooleanField(required=False, label="Editar")
    delete_seguro = forms.BooleanField(required=False, label="Excluir")
    
    add_sinistro = forms.BooleanField(required=False, label="Adicionar")
    change_sinistro = forms.BooleanField(required=False, label="Editar")
    delete_sinistro = forms.BooleanField(required=False, label="Excluir")
    
    add_veiculoassegurado = forms.BooleanField(required=False, label="Adicionar")
    change_veiculoassegurado = forms.BooleanField(required=False, label="Editar")
    delete_veiculoassegurado = forms.BooleanField(required=False, label="Excluir")
    
    add_securitytarefa = forms.BooleanField(required=False, label="Adicionar")
    change_securitytarefa = forms.BooleanField(required=False, label="Editar")
    delete_securitytarefa = forms.BooleanField(required=False, label="Excluir")
    
    # QSMS
    view_qsms_module = forms.BooleanField(required=False, label="Visualizar mÃ³dulo")
    view_qsms_attachments = forms.BooleanField(required=False, label="Visualizar anexos")
    add_certificadoqsms = forms.BooleanField(required=False, label="Adicionar")
    change_certificadoqsms = forms.BooleanField(required=False, label="Editar")
    delete_certificadoqsms = forms.BooleanField(required=False, label="Excluir")
    
    add_agendaqsms = forms.BooleanField(required=False, label="Adicionar")
    change_agendaqsms = forms.BooleanField(required=False, label="Editar")
    delete_agendaqsms = forms.BooleanField(required=False, label="Excluir")
    
    add_qsmstarefa = forms.BooleanField(required=False, label="Adicionar")
    change_qsmstarefa = forms.BooleanField(required=False, label="Editar")
    delete_qsmstarefa = forms.BooleanField(required=False, label="Excluir")
    
    # FÃRMACO
    view_farmaco_module = forms.BooleanField(required=False, label="Visualizar mÃ³dulo")
    view_farmaco_attachments = forms.BooleanField(required=False, label="Visualizar anexos")
    add_certificadofarmaco = forms.BooleanField(required=False, label="Adicionar")
    change_certificadofarmaco = forms.BooleanField(required=False, label="Editar")
    delete_certificadofarmaco = forms.BooleanField(required=False, label="Excluir")
    
    add_agendafarmaco = forms.BooleanField(required=False, label="Adicionar")
    change_agendafarmaco = forms.BooleanField(required=False, label="Editar")
    delete_agendafarmaco = forms.BooleanField(required=False, label="Excluir")
    
    add_farmacotarefa = forms.BooleanField(required=False, label="Adicionar")
    change_farmacotarefa = forms.BooleanField(required=False, label="Editar")
    delete_farmacotarefa = forms.BooleanField(required=False, label="Excluir")
    
    # ARQUIVOS DIVERSOS
    view_arquivosdiversos_module = forms.BooleanField(required=False, label="Visualizar mÃ³dulo")
    view_all_arquivodiverso = forms.BooleanField(required=False, label="Visualizar todos")
    add_arquivodiverso = forms.BooleanField(required=False, label="Adicionar")
    change_arquivodiverso = forms.BooleanField(required=False, label="Editar")
    delete_arquivodiverso = forms.BooleanField(required=False, label="Excluir")
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'username': 'Nome de UsuÃ¡rio',
            'email': 'E-mail',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'is_staff': 'Ã Administrador?',
            'is_active': 'UsuÃ¡rio Ativo?',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            # Carregar permissÃµes atuais do usuÃ¡rio
            user_permissions = self.instance.user_permissions.all()
            perm_codenames = [p.codename for p in user_permissions]
            
            # Marcar checkboxes das permissÃµes que o usuÃ¡rio tem
            for field_name in self.fields:
                if field_name in perm_codenames:
                    self.fields[field_name].initial = True
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        if password1 and password1 != password2:
            raise forms.ValidationError('As senhas nÃ£o coincidem.')
        
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        
        # Se Ã© novo usuÃ¡rio e nÃ£o forneceu senha, usar padrÃ£o
        if not self.instance.pk:
            password = self.cleaned_data.get('password1')
            if password:
                user.set_password(password)
            else:
                user.set_password('transbirday2025')  # Senha padrÃ£o
        else:
            # Se estÃ¡ editando e forneceu nova senha
            password = self.cleaned_data.get('password1')
            if password:
                user.set_password(password)
        
        if commit:
            user.save()
            
            # Limpar permissÃµes antigas
            user.user_permissions.clear()
            
            # Lista de campos que nÃ£o sÃ£o permissÃµes
            non_perm_fields = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'password1', 'password2']
            
            # Adicionar novas permissÃµes
            for field_name in self.fields:
                if field_name not in non_perm_fields and self.cleaned_data.get(field_name):
                    try:
                        permission = Permission.objects.get(codename=field_name)
                        user.user_permissions.add(permission)
                    except Permission.DoesNotExist:
                        pass
        
        return user
