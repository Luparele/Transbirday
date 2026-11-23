from datetime import date
from django.contrib import admin
from django.utils.html import format_html

from .models import (
    PGR,
    RegraEmbarque,
    Veiculo,
    GerenciadoraRisco,
    Checklist,
    Rotograma,
    CondutorBlacklist,
    Tarefa,
    HistoricoTarefa,
    SecurityTarefa,
    SecurityHistoricoTarefa,
    Seguro,
    Sinistro,
    VeiculoAssegurado,
    CertificadoQSMS,
    AgendaQSMS,
    QsmsTarefa,
    QsmsHistoricoTarefa,
    ArquivoDiverso,
    CertificadoFarmaco,
    AgendaFarmaco,
    FarmacoTarefa,
    FarmacoHistoricoTarefa,
    DocumentacaoAgregado,
    AgregadoHistorico,
)

admin.site.site_header = "Transbirday — Administração"
admin.site.site_title = "Transbirday Admin"
admin.site.index_title = "Painel Administrativo do Sistema"


def _status_validade_badge(validade_date):
    """Retorna badge HTML com status de vencimento para colunas de list_display."""
    if not validade_date:
        return "-"
    dias = (validade_date - date.today()).days
    if dias < 0:
        return format_html('<span style="color:#b02a37;font-weight:bold;">Vencido ({}d)</span>', abs(dias))
    if dias <= 30:
        return format_html('<span style="color:#dc3545;font-weight:bold;">Vence em {}d</span>', dias)
    if dias <= 89:
        return format_html('<span style="color:#cc7a00;font-weight:bold;">{}d restantes</span>', dias)
    return format_html('<span style="color:#198754;font-weight:bold;">Em dia ({}d)</span>', dias)


# ===================================================================
#           INLINES DE HISTÓRICO E RELACIONAMENTOS
# ===================================================================

class HistoricoTarefaInline(admin.TabularInline):
    model = HistoricoTarefa
    extra = 0
    readonly_fields = ('usuario', 'acao', 'timestamp')
    can_delete = False


class SecurityHistoricoTarefaInline(admin.TabularInline):
    model = SecurityHistoricoTarefa
    extra = 0
    readonly_fields = ('usuario', 'acao', 'timestamp')
    can_delete = False


class QsmsHistoricoTarefaInline(admin.TabularInline):
    model = QsmsHistoricoTarefa
    extra = 0
    readonly_fields = ('usuario', 'acao', 'timestamp')
    can_delete = False


class FarmacoHistoricoTarefaInline(admin.TabularInline):
    model = FarmacoHistoricoTarefa
    extra = 0
    readonly_fields = ('usuario', 'acao', 'timestamp')
    can_delete = False


class AgregadoHistoricoInline(admin.TabularInline):
    model = AgregadoHistorico
    extra = 0
    readonly_fields = ('usuario', 'acao', 'timestamp')
    can_delete = False


class ChecklistInline(admin.TabularInline):
    model = Checklist
    extra = 0
    fields = ('gerenciadora', 'aprovado', 'data_aprovacao', 'data_fim_validade', 'ultimo_usuario')
    readonly_fields = ('ultimo_usuario',)


# ===================================================================
#           MÓDULO GR / OPERACIONAL
# ===================================================================

@admin.register(RegraEmbarque)
class RegraEmbarqueAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'resumo_descricao')
    search_fields = ('titulo', 'descricao')
    ordering = ('titulo',)
    list_per_page = 25

    @admin.display(description="Descrição")
    def resumo_descricao(self, obj):
        return (obj.descricao[:80] + '...') if len(obj.descricao) > 80 else obj.descricao


@admin.register(PGR)
class PGRAdmin(admin.ModelAdmin):
    list_display = ('titulo_cliente', 'tipo_seguro', 'validade', 'status_validade', 'gerente_conta', 'contato_gc', 'tem_pdf', 'responsavel_cadastro')
    list_filter = ('tipo_seguro', 'validade', 'responsavel_cadastro')
    search_fields = ('titulo_cliente', 'gerente_conta', 'email_gc', 'contato_gc')
    filter_horizontal = ('regras_embarque',)
    date_hierarchy = 'validade'
    ordering = ('validade',)
    list_select_related = ('responsavel_cadastro',)
    list_per_page = 25

    @admin.display(description="Status", ordering='validade')
    def status_validade(self, obj):
        return _status_validade_badge(obj.validade)

    @admin.display(description="PDF", boolean=True)
    def tem_pdf(self, obj):
        return bool(obj.arquivo_pdf)


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'categoria', 'tipo')
    list_filter = ('categoria', 'tipo')
    search_fields = ('placa',)
    ordering = ('placa',)
    inlines = [ChecklistInline]
    list_per_page = 30


@admin.register(GerenciadoraRisco)
class GerenciadoraRiscoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'validade_checklist')
    list_filter = ('validade_checklist',)
    search_fields = ('nome',)
    ordering = ('nome',)


@admin.register(Checklist)
class ChecklistAdmin(admin.ModelAdmin):
    list_display = ('veiculo', 'gerenciadora', 'aprovado', 'data_aprovacao', 'data_fim_validade', 'status_validade', 'ultimo_usuario')
    list_filter = ('aprovado', 'gerenciadora', 'veiculo__categoria', 'veiculo__tipo', 'data_fim_validade')
    search_fields = ('veiculo__placa', 'gerenciadora__nome', 'motivo_reprovacao')
    date_hierarchy = 'data_fim_validade'
    ordering = ('data_fim_validade',)
    list_select_related = ('veiculo', 'gerenciadora', 'ultimo_usuario')
    list_per_page = 30

    @admin.display(description="Status", ordering='data_fim_validade')
    def status_validade(self, obj):
        return _status_validade_badge(obj.data_fim_validade)


@admin.register(Rotograma)
class RotogramaAdmin(admin.ModelAdmin):
    list_display = ('nome_titulo', 'origem', 'destino', 'tem_pdf')
    search_fields = ('nome_titulo', 'origem', 'destino')
    list_filter = ('origem', 'destino')
    ordering = ('nome_titulo',)
    list_per_page = 25

    @admin.display(description="PDF", boolean=True)
    def tem_pdf(self, obj):
        return bool(obj.arquivo_pdf)


@admin.register(CondutorBlacklist)
class CondutorBlacklistAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cpf', 'data_pesquisa', 'responsavel_cadastro', 'criado_em')
    search_fields = ('nome_completo', 'cpf', 'motivo_reprovacao')
    list_filter = ('data_pesquisa', 'responsavel_cadastro')
    date_hierarchy = 'data_pesquisa'
    readonly_fields = ('criado_em',)
    ordering = ('-data_pesquisa',)
    list_select_related = ('responsavel_cadastro',)
    list_per_page = 25


# ===================================================================
#           TAREFAS E HISTÓRICOS (GR / SECURITY / QSMS / FÁRMACO)
# ===================================================================

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'autor', 'criado_em')
    list_filter = ('status', 'autor', 'criado_em')
    search_fields = ('titulo', 'descricao')
    readonly_fields = ('criado_em',)
    date_hierarchy = 'criado_em'
    ordering = ('-criado_em',)
    list_select_related = ('autor',)
    inlines = [HistoricoTarefaInline]
    list_per_page = 25


@admin.register(HistoricoTarefa)
class HistoricoTarefaAdmin(admin.ModelAdmin):
    list_display = ('tarefa', 'usuario', 'acao', 'timestamp')
    list_filter = ('usuario', 'timestamp')
    search_fields = ('tarefa__titulo', 'acao')
    readonly_fields = ('timestamp',)
    ordering = ('-timestamp',)
    list_select_related = ('tarefa', 'usuario')


@admin.register(SecurityTarefa)
class SecurityTarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'autor', 'criado_em')
    list_filter = ('status', 'autor', 'criado_em')
    search_fields = ('titulo', 'descricao')
    readonly_fields = ('criado_em',)
    date_hierarchy = 'criado_em'
    ordering = ('-criado_em',)
    list_select_related = ('autor',)
    inlines = [SecurityHistoricoTarefaInline]
    list_per_page = 25


@admin.register(SecurityHistoricoTarefa)
class SecurityHistoricoTarefaAdmin(admin.ModelAdmin):
    list_display = ('tarefa', 'usuario', 'acao', 'timestamp')
    list_filter = ('usuario', 'timestamp')
    search_fields = ('tarefa__titulo', 'acao')
    readonly_fields = ('timestamp',)
    ordering = ('-timestamp',)
    list_select_related = ('tarefa', 'usuario')


# ===================================================================
#           SEGUROS E SINISTROS
# ===================================================================

@admin.register(Seguro)
class SeguroAdmin(admin.ModelAdmin):
    list_display = ('seguradora', 'tipo_apolice', 'corretora', 'corretor', 'vigencia', 'status_vigencia', 'tem_apolice', 'tem_certificado', 'responsavel_cadastro')
    list_filter = ('seguradora', 'corretora', 'vigencia', 'responsavel_cadastro')
    search_fields = ('seguradora', 'tipo_apolice', 'corretora', 'corretor', 'email_corretor')
    date_hierarchy = 'vigencia'
    ordering = ('vigencia',)
    list_select_related = ('responsavel_cadastro',)
    list_per_page = 25

    @admin.display(description="Status", ordering='vigencia')
    def status_vigencia(self, obj):
        return _status_validade_badge(obj.vigencia)

    @admin.display(description="Apólice", boolean=True)
    def tem_apolice(self, obj):
        return bool(obj.apolice_pdf)

    @admin.display(description="Certificado", boolean=True)
    def tem_certificado(self, obj):
        return bool(obj.certificado_pdf)


@admin.register(Sinistro)
class SinistroAdmin(admin.ModelAdmin):
    list_display = ('data_sinistro', 'hora_sinistro', 'seguradora_responsavel', 'status', 'responsavel_cadastro')
    list_filter = ('status', 'seguradora_responsavel', 'data_sinistro', 'responsavel_cadastro')
    search_fields = ('seguradora_responsavel', 'detalhes')
    date_hierarchy = 'data_sinistro'
    ordering = ('-data_sinistro', '-hora_sinistro')
    list_select_related = ('responsavel_cadastro',)
    list_per_page = 25


@admin.register(VeiculoAssegurado)
class VeiculoAsseguradoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'marca', 'modelo', 'ano_fabricacao', 'ano_modelo', 'seguradora', 'cobertura', 'vigencia', 'status_vigencia', 'cobertura_vidros')
    list_filter = ('seguradora', 'cobertura', 'cobertura_vidros', 'vigencia', 'responsavel_cadastro')
    search_fields = ('placa', 'marca', 'modelo', 'seguradora')
    date_hierarchy = 'vigencia'
    ordering = ('vigencia', 'placa')
    list_select_related = ('responsavel_cadastro',)
    list_per_page = 25

    @admin.display(description="Status", ordering='vigencia')
    def status_vigencia(self, obj):
        return _status_validade_badge(obj.vigencia)


# ===================================================================
#           MÓDULO QSMS
# ===================================================================

@admin.register(CertificadoQSMS)
class CertificadoQSMSAdmin(admin.ModelAdmin):
    list_display = ('certificado', 'orgao_competente', 'validade', 'status_validade', 'tem_pdf', 'responsavel_cadastro')
    list_filter = ('orgao_competente', 'validade', 'responsavel_cadastro')
    search_fields = ('certificado', 'orgao_competente', 'descricao')
    date_hierarchy = 'validade'
    ordering = ('validade',)
    list_select_related = ('responsavel_cadastro',)
    list_per_page = 25

    @admin.display(description="Status", ordering='validade')
    def status_validade(self, obj):
        return _status_validade_badge(obj.validade)

    @admin.display(description="PDF", boolean=True)
    def tem_pdf(self, obj):
        return bool(obj.arquivo_pdf)


@admin.register(AgendaQSMS)
class AgendaQSMSAdmin(admin.ModelAdmin):
    list_display = ('assunto', 'tipo', 'data_evento', 'hora_evento', 'responsavel_cadastro')
    list_filter = ('tipo', 'data_evento', 'responsavel_cadastro')
    search_fields = ('assunto', 'detalhes')
    date_hierarchy = 'data_evento'
    ordering = ('data_evento', 'hora_evento')
    list_select_related = ('responsavel_cadastro',)
    list_per_page = 25


@admin.register(QsmsTarefa)
class QsmsTarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'autor', 'criado_em')
    list_filter = ('status', 'autor', 'criado_em')
    search_fields = ('titulo', 'descricao')
    readonly_fields = ('criado_em',)
    date_hierarchy = 'criado_em'
    ordering = ('-criado_em',)
    list_select_related = ('autor',)
    inlines = [QsmsHistoricoTarefaInline]
    list_per_page = 25


@admin.register(QsmsHistoricoTarefa)
class QsmsHistoricoTarefaAdmin(admin.ModelAdmin):
    list_display = ('tarefa', 'usuario', 'acao', 'timestamp')
    list_filter = ('usuario', 'timestamp')
    search_fields = ('tarefa__titulo', 'acao')
    readonly_fields = ('timestamp',)
    ordering = ('-timestamp',)
    list_select_related = ('tarefa', 'usuario')


# ===================================================================
#           ARQUIVOS DIVERSOS
# ===================================================================

@admin.register(ArquivoDiverso)
class ArquivoDiversoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tem_pdf', 'responsavel_cadastro', 'criado_em')
    list_filter = ('criado_em', 'responsavel_cadastro')
    search_fields = ('titulo', 'descricao')
    readonly_fields = ('criado_em',)
    date_hierarchy = 'criado_em'
    ordering = ('-criado_em',)
    list_select_related = ('responsavel_cadastro',)
    list_per_page = 25

    @admin.display(description="PDF", boolean=True)
    def tem_pdf(self, obj):
        return bool(obj.arquivo_pdf)


# ===================================================================
#           MÓDULO FÁRMACO
# ===================================================================

@admin.register(CertificadoFarmaco)
class CertificadoFarmacoAdmin(admin.ModelAdmin):
    list_display = ('certificado', 'orgao_competente', 'validade', 'status_validade', 'tem_pdf', 'responsavel_cadastro')
    search_fields = ('certificado', 'orgao_competente', 'descricao')
    list_filter = ('orgao_competente', 'validade', 'responsavel_cadastro')
    date_hierarchy = 'validade'
    ordering = ('validade',)
    list_select_related = ('responsavel_cadastro',)
    list_per_page = 25

    @admin.display(description="Status", ordering='validade')
    def status_validade(self, obj):
        return _status_validade_badge(obj.validade)

    @admin.display(description="PDF", boolean=True)
    def tem_pdf(self, obj):
        return bool(obj.arquivo_pdf)


@admin.register(AgendaFarmaco)
class AgendaFarmacoAdmin(admin.ModelAdmin):
    list_display = ('assunto', 'tipo', 'data_evento', 'hora_evento', 'responsavel_cadastro')
    search_fields = ('assunto', 'detalhes')
    list_filter = ('tipo', 'data_evento', 'responsavel_cadastro')
    date_hierarchy = 'data_evento'
    ordering = ('data_evento', 'hora_evento')
    list_select_related = ('responsavel_cadastro',)
    list_per_page = 25


@admin.register(FarmacoTarefa)
class FarmacoTarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'autor', 'criado_em')
    list_filter = ('status', 'autor', 'criado_em')
    search_fields = ('titulo', 'descricao')
    readonly_fields = ('criado_em',)
    date_hierarchy = 'criado_em'
    ordering = ('-criado_em',)
    list_select_related = ('autor',)
    inlines = [FarmacoHistoricoTarefaInline]
    list_per_page = 25


@admin.register(FarmacoHistoricoTarefa)
class FarmacoHistoricoTarefaAdmin(admin.ModelAdmin):
    list_display = ('tarefa', 'usuario', 'acao', 'timestamp')
    list_filter = ('usuario', 'timestamp')
    search_fields = ('tarefa__titulo', 'acao')
    readonly_fields = ('timestamp',)
    ordering = ('-timestamp',)
    list_select_related = ('tarefa', 'usuario')


# ===================================================================
#           AGREGADOS
# ===================================================================

@admin.register(DocumentacaoAgregado)
class DocumentacaoAgregadoAdmin(admin.ModelAdmin):
    list_display = (
        'placa', 'condutor', 'crlv_ano',
        'dedetizacao_validade', 'status_dedetizacao',
        'limpeza_validade', 'status_limpeza',
        'responsavel_cadastro', 'criado_em'
    )
    search_fields = ('placa', 'condutor')
    list_filter = ('crlv_ano', 'dedetizacao_validade', 'limpeza_validade', 'criado_em', 'responsavel_cadastro')
    readonly_fields = ('criado_em',)
    date_hierarchy = 'criado_em'
    ordering = ('placa',)
    list_select_related = ('responsavel_cadastro',)
    inlines = [AgregadoHistoricoInline]
    list_per_page = 25

    @admin.display(description="Dedetização", ordering='dedetizacao_validade')
    def status_dedetizacao(self, obj):
        return _status_validade_badge(obj.dedetizacao_validade)

    @admin.display(description="Limpeza", ordering='limpeza_validade')
    def status_limpeza(self, obj):
        return _status_validade_badge(obj.limpeza_validade)


@admin.register(AgregadoHistorico)
class AgregadoHistoricoAdmin(admin.ModelAdmin):
    list_display = ('agregado', 'usuario', 'acao', 'timestamp')
    search_fields = ('agregado__placa', 'agregado__condutor', 'acao')
    list_filter = ('usuario', 'timestamp')
    readonly_fields = ('timestamp',)
    ordering = ('-timestamp',)
    list_select_related = ('agregado', 'usuario')
