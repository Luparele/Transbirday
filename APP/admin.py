from django.contrib import admin
from .models import (
    PGR, 
    RegraEmbarque, 
    Veiculo, 
    GerenciadoraRisco, 
    Checklist, 
    Rotograma, 
    # ===================================================================
    #                       INÍCIO DAS ADIÇÕES
    # ===================================================================
    CondutorBlacklist,
    # ===================================================================
    #                         FIM DAS ADIÇÕES
    # ===================================================================
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
    # ===================================================================
    #                    MODELOS DO FÁRMACO
    # ===================================================================
    CertificadoFarmaco,
    AgendaFarmaco,
    FarmacoTarefa,
    FarmacoHistoricoTarefa,
    # ===================================================================
    #                         FIM FÁRMACO
    # ===================================================================
)

# Customização do Admin para Tarefas
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'autor', 'criado_em')
    list_filter = ('status', 'autor')
    search_fields = ('titulo', 'descricao')

class SecurityTarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'autor', 'criado_em')
    list_filter = ('status', 'autor')
    search_fields = ('titulo', 'descricao')

class QsmsTarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'autor', 'criado_em')
    list_filter = ('status', 'autor')
    search_fields = ('titulo', 'descricao')

# ===================================================================
#           INÍCIO DO NOVO ADMIN (BLACK LIST)
# ===================================================================
class CondutorBlacklistAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cpf', 'data_pesquisa', 'responsavel_cadastro')
    search_fields = ('nome_completo', 'cpf')
    list_filter = ('data_pesquisa', 'responsavel_cadastro')
# ===================================================================
#                         FIM DAS ADIÇÕES
# ===================================================================

# ===================================================================
#           ADMIN CUSTOMIZADO PARA FÁRMACO
# ===================================================================
class CertificadoFarmacoAdmin(admin.ModelAdmin):
    list_display = ('certificado', 'orgao_competente', 'validade', 'responsavel_cadastro')
    search_fields = ('certificado', 'orgao_competente')
    list_filter = ('validade', 'responsavel_cadastro')
    ordering = ('validade',)

class AgendaFarmacoAdmin(admin.ModelAdmin):
    list_display = ('assunto', 'tipo', 'data_evento', 'hora_evento', 'responsavel_cadastro')
    search_fields = ('assunto', 'detalhes')
    list_filter = ('tipo', 'data_evento', 'responsavel_cadastro')
    ordering = ('data_evento', 'hora_evento')

class FarmacoTarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'autor', 'criado_em')
    list_filter = ('status', 'autor')
    search_fields = ('titulo', 'descricao')
    ordering = ('-criado_em',)

class FarmacoHistoricoTarefaAdmin(admin.ModelAdmin):
    list_display = ('tarefa', 'usuario', 'timestamp')
    list_filter = ('usuario', 'timestamp')
    search_fields = ('tarefa__titulo', 'acao')
    ordering = ('timestamp',)
# ===================================================================
#                         FIM ADMIN FÁRMACO
# ===================================================================

# Registrando os modelos
admin.site.register(PGR)
admin.site.register(RegraEmbarque)
admin.site.register(Veiculo)
admin.site.register(GerenciadoraRisco)
admin.site.register(Checklist)
admin.site.register(Rotograma)
# ===================================================================
#           INÍCIO DO REGISTO (BLACK LIST)
# ===================================================================
admin.site.register(CondutorBlacklist, CondutorBlacklistAdmin)
# ===================================================================
#                         FIM DAS ADIÇÕES
# ===================================================================
admin.site.register(Seguro)
admin.site.register(Sinistro)
admin.site.register(VeiculoAssegurado)

# Registra os modelos de tarefas
admin.site.register(Tarefa, TarefaAdmin) # Tarefas de GR
admin.site.register(HistoricoTarefa) # Histórico de GR
admin.site.register(SecurityTarefa, SecurityTarefaAdmin) # Novas Tarefas de Security
admin.site.register(SecurityHistoricoTarefa) # Novo Histórico de Security

# REGISTO DOS MODELOS QSMS
admin.site.register(CertificadoQSMS)
admin.site.register(AgendaQSMS)
admin.site.register(QsmsTarefa, QsmsTarefaAdmin)
admin.site.register(QsmsHistoricoTarefa)

# REGISTO DE ARQUIVOS DIVERSOS
admin.site.register(ArquivoDiverso)

# ===================================================================
#           REGISTO DOS MODELOS DO FÁRMACO
# ===================================================================
admin.site.register(CertificadoFarmaco, CertificadoFarmacoAdmin)
admin.site.register(AgendaFarmaco, AgendaFarmacoAdmin)
admin.site.register(FarmacoTarefa, FarmacoTarefaAdmin)
admin.site.register(FarmacoHistoricoTarefa, FarmacoHistoricoTarefaAdmin)
# ===================================================================
#                         FIM REGISTO FÁRMACO
# ===================================================================