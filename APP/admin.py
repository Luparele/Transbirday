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
    ArquivoDiverso
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