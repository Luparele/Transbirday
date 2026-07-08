from django.db import models
from django.contrib.auth.models import User
# ===================================================================
#                       INÍCIO DAS ADIÇÕES
# ===================================================================
from django.core.validators import RegexValidator
# ===================================================================
#                         FIM DAS ADIÇÕES
# ===================================================================

# GR – Gerenciamento de Risco
class RegraEmbarque(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo

class PGR(models.Model):
    class TipoSeguro(models.TextChoices):
        PROPRIO = 'Próprio', 'Próprio'
        DDR = 'DDR', 'DDR'
    titulo_cliente = models.CharField(max_length=255, verbose_name="Título do PGR (Cliente)")
    validade = models.DateField(verbose_name="Validade")
    gerente_conta = models.CharField(max_length=100, blank=True, null=True, verbose_name="Gerente de Conta")
    contato_gc = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefone de Contato do GC")
    email_gc = models.EmailField(blank=True, null=True, verbose_name="E-mail do GC")
    tipo_seguro = models.CharField(max_length=10, choices=TipoSeguro.choices, verbose_name="Tipo de Seguro")
    arquivo_pdf = models.FileField(upload_to='pgr_pdfs/', verbose_name="Arquivo PDF do PGR")
    regras_embarque = models.ManyToManyField(RegraEmbarque, blank=True)
    responsavel_cadastro = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="pgrs_cadastrados")
    
    def __str__(self):
        return self.titulo_cliente

class Veiculo(models.Model):
    class Categoria(models.TextChoices):
        FROTA = 'Frota', 'Frota'
        AGREGADO = 'Agregado', 'Agregado'
    class Tipo(models.TextChoices):
        CAVALO = 'Cavalo Mecanico', 'Cavalo Mecanico'
        CARRETA = 'Carreta', 'Carreta'
    placa = models.CharField(max_length=10, unique=True)
    categoria = models.CharField(max_length=10, choices=Categoria.choices)
    tipo = models.CharField(max_length=20, choices=Tipo.choices)
    
    def __str__(self):
        return self.placa

class GerenciadoraRisco(models.Model):
    class Validade(models.IntegerChoices):
        TRINTA = 30, '30 dias'
        SESSENTA = 60, '60 dias'
        NOVENTA = 90, '90 dias'
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome da GR")
    validade_checklist = models.IntegerField(choices=Validade.choices, verbose_name="Validade")

    def __str__(self):
        return self.nome

class Checklist(models.Model):
    class Aprovado(models.TextChoices):
        SIM = 'Sim', 'Sim'
        NAO = 'Nao', 'Nao'
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    gerenciadora = models.ForeignKey(GerenciadoraRisco, on_delete=models.CASCADE, verbose_name="GR")
    aprovado = models.CharField(max_length=5, choices=Aprovado.choices)
    data_aprovacao = models.DateField(blank=True, null=True, verbose_name="Data de Aprovacao/Realizacao")
    data_fim_validade = models.DateField(blank=True, null=True, verbose_name="Validade")
    motivo_reprovacao = models.TextField(blank=True, null=True)
    ultimo_usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="checklists_alterados")
    class Meta:
        unique_together = ('veiculo', 'gerenciadora')
    def __str__(self):
        return f"{self.veiculo.placa} - {self.gerenciadora.nome}"

class Rotograma(models.Model):
    nome_titulo = models.CharField(max_length=255, verbose_name="Nome/Título")
    origem = models.CharField(max_length=150)
    destino = models.CharField(max_length=150)
    arquivo_pdf = models.FileField(upload_to='rotogramas_pdfs/', verbose_name="Arquivo PDF do Rotograma")

    def __str__(self):
        return self.nome_titulo

# ===================================================================
#           INÍCIO DO NOVO MODELO (BLACK LIST)
# ===================================================================
class CondutorBlacklist(models.Model):
    cpf_validator = RegexValidator(
        regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
        message='O CPF deve estar no formato XXX.XXX.XXX-XX.'
    )
    
    nome_completo = models.CharField(max_length=255, verbose_name="Nome Completo")
    cpf = models.CharField(max_length=14, unique=True, validators=[cpf_validator], verbose_name="CPF")
    data_pesquisa = models.DateField(verbose_name="Data da Pesquisa")
    motivo_reprovacao = models.TextField(verbose_name="Motivo da Reprovação")
    responsavel_cadastro = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="condutores_blacklist_cadastrados")
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nome_completo']
        verbose_name = "Condutor (Blacklist)"
        verbose_name_plural = "Condutores (Blacklist)"

    def __str__(self):
        return f"{self.nome_completo} ({self.cpf})"
# ===================================================================
#                         FIM DAS ADIÇÕES
# ===================================================================

# Modelos de Tarefa de GR (EXISTENTES)
class Tarefa(models.Model):
    class Status(models.TextChoices):
        PENDENTE = 'Pendente', 'Pendente'
        INICIADA = 'Iniciada', 'Iniciada'
        FINALIZADA = 'Finalizada', 'Finalizada'
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.PENDENTE)
    criado_em = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return self.titulo

class HistoricoTarefa(models.Model):
    tarefa = models.ForeignKey(Tarefa, related_name='historico', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    acao = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"{self.tarefa.titulo} - {self.timestamp.strftime('%d/%m/%Y %H:%M')}"

# ===================================================================
#           MODELOS DE SECURITY
# ===================================================================
class SecurityTarefa(models.Model):
    class Status(models.TextChoices):
        PENDENTE = 'Pendente', 'Pendente'
        INICIADA = 'Iniciada', 'Iniciada'
        FINALIZADA = 'Finalizada', 'Finalizada'

    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.PENDENTE)
    criado_em = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-criado_em']
        verbose_name = "Tarefa de Security"
        verbose_name_plural = "Tarefas de Security"

    def __str__(self):
        return self.titulo

class SecurityHistoricoTarefa(models.Model):
    tarefa = models.ForeignKey(SecurityTarefa, related_name='historico', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    acao = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['timestamp']
        verbose_name = "Histórico de Tarefa de Security"
        verbose_name_plural = "Históricos de Tarefas de Security"

    def __str__(self):
        return f"[Security] {self.tarefa.titulo} - {self.timestamp.strftime('%d/%m/%Y %H:%M')}"

class Seguro(models.Model):
    seguradora = models.CharField(max_length=100)
    tipo_apolice = models.CharField(max_length=100, verbose_name="Tipo de Apólice")
    corretora = models.CharField(max_length=100)
    corretor = models.CharField(max_length=100)
    contato_corretor = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefone de Contato")
    email_corretor = models.EmailField(blank=True, null=True, verbose_name="E-mail do Corretor")
    vigencia = models.DateField(verbose_name="Vigencia")
    descricao_resumo = models.TextField(blank=True, null=True, verbose_name="Descricao")
    apolice_pdf = models.FileField(upload_to='seguros/apolices/', verbose_name="Upload da Apólice (PDF)")
    certificado_pdf = models.FileField(upload_to='seguros/certificados/', verbose_name="Upload do Certificado (PDF)")
    responsavel_cadastro = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="seguros_cadastrados")

    def __str__(self):
        return f"{self.seguradora} - {self.tipo_apolice}"

class Sinistro(models.Model):
    class StatusSinistro(models.TextChoices):
        EM_ANDAMENTO = 'Em andamento', 'Em andamento'
        FINALIZADO = 'Finalizado', 'Finalizado'
    data_sinistro = models.DateField(verbose_name="Data do Sinistro")
    hora_sinistro = models.TimeField(verbose_name="Hora do Sinistro")
    seguradora_responsavel = models.CharField(max_length=100, verbose_name="Seguradora Responsável")
    status = models.CharField(max_length=20, choices=StatusSinistro.choices, default=StatusSinistro.EM_ANDAMENTO)
    detalhes = models.TextField(verbose_name="Detalhes")
    responsavel_cadastro = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="sinistros_cadastrados")

    def __str__(self):
        return f"Sinistro em {self.data_sinistro} - {self.seguradora_responsavel}"

class VeiculoAssegurado(models.Model):
    class CoberturaTipo(models.TextChoices):
        TOTAL = 'Total', 'Total'
        TERCEIROS = 'Apenas Terceiros', 'Apenas Terceiros'
    seguradora = models.CharField(max_length=100)
    vigencia = models.DateField(verbose_name="Vigencia")
    placa = models.CharField(max_length=10)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano_fabricacao = models.IntegerField(verbose_name="Ano de Fabricação")
    ano_modelo = models.IntegerField(verbose_name="Ano do Modelo")
    cobertura = models.CharField(max_length=20, choices=CoberturaTipo.choices, default=CoberturaTipo.TOTAL)
    valor_fipe_percent = models.IntegerField(verbose_name="Valor FIPE (%)")
    franquia = models.DecimalField(max_digits=10, decimal_places=2)
    danos_materiais = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Danos Materiais")
    danos_corporais = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Danos Corporais")
    danos_morais = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Danos Morais")
    app_morte = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="APP Morte")
    app_invalidez = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="APP Invalidez")
    assistencia_km = models.IntegerField(verbose_name="Reboque/Assistência 24h (KM)")
    carro_reserva_dias = models.IntegerField(verbose_name="Carro Reserva (dias)")
    cobertura_vidros = models.BooleanField(default=False, verbose_name="Cobertura extra para vidros")
    responsavel_cadastro = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="veiculos_assegurados_cadastrados")

    def __str__(self):
        return f"{self.placa} ({self.modelo}) - {self.seguradora}"

# ===================================================================
#           MODELOS DE QSMS
# ===================================================================
class CertificadoQSMS(models.Model):
    certificado = models.CharField(max_length=255, verbose_name="Certificado") 
    orgao_competente = models.CharField(max_length=255, verbose_name="Órgão Competente") 
    link_orgao = models.URLField(max_length=255, blank=True, null=True, verbose_name="Link do Órgão") 
    validade = models.DateField(verbose_name="Validade") 
    arquivo_pdf = models.FileField(upload_to='qsms/certificados_pdf/', verbose_name="Upload de Certificado PDF") 
    descricao = models.TextField(blank=True, null=True, verbose_name="Descricao") 
    responsavel_cadastro = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="certificados_qsms_cadastrados")

    class Meta:
        ordering = ['validade']
        verbose_name = "Certificado QSMS"
        verbose_name_plural = "Certificados QSMS"

    def __str__(self):
        return self.certificado

class AgendaQSMS(models.Model):
    class TipoEvento(models.TextChoices):
        TREINAMENTO = 'Treinamento', 'Treinamento'
        EVENTO = 'Evento', 'Evento'

    tipo = models.CharField(max_length=20, choices=TipoEvento.choices, default=TipoEvento.TREINAMENTO)
    assunto = models.CharField(max_length=255, verbose_name="Assunto")
    data_evento = models.DateField(verbose_name="Data do Evento")
    hora_evento = models.TimeField(verbose_name="Hora do Evento")
    detalhes = models.TextField(blank=True, null=True, verbose_name="Detalhes")
    responsavel_cadastro = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="eventos_qsms_cadastrados")

    class Meta:
        ordering = ['data_evento', 'hora_evento']
        verbose_name = "Evento da Agenda QSMS"
        verbose_name_plural = "Eventos da Agenda QSMS"

    def __str__(self):
        return f"[{self.get_tipo_display()}] {self.assunto} em {self.data_evento}"

class QsmsTarefa(models.Model):
    class Status(models.TextChoices):
        PENDENTE = 'Pendente', 'Pendente'
        INICIADA = 'Iniciada', 'Iniciada'
        FINALIZADA = 'Finalizada', 'Finalizada'

    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.PENDENTE)
    criado_em = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-criado_em']
        verbose_name = "Tarefa de QSMS"
        verbose_name_plural = "Tarefas de QSMS"

    def __str__(self):
        return self.titulo

class QsmsHistoricoTarefa(models.Model):
    tarefa = models.ForeignKey(QsmsTarefa, related_name='historico', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    acao = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['timestamp']
        verbose_name = "Histórico de Tarefa de QSMS"
        verbose_name_plural = "Históricos de Tarefas de QSMS"

    def __str__(self):
        return f"[QSMS] {self.tarefa.titulo} - {self.timestamp.strftime('%d/%m/%Y %H:%M')}"

class DocumentacaoAgregado(models.Model):
    placa = models.CharField(max_length=10, unique=True, verbose_name="Placa")
    condutor = models.CharField(max_length=255, verbose_name="Condutor Responsável")
    crlv_ano = models.IntegerField(verbose_name="Ano em Exercício (CRLV)")
    crlv_pdf = models.FileField(upload_to='qsms/agregados/crlv/', verbose_name="CRLV (PDF)")
    
    dedetizacao_validade = models.DateField(blank=True, null=True, verbose_name="Validade da Dedetização")
    dedetizacao_pdf = models.FileField(upload_to='qsms/agregados/dedetizacao/', blank=True, null=True, verbose_name="Comprovante de Dedetização (PDF)")
    
    limpeza_validade = models.DateField(blank=True, null=True, verbose_name="Validade da Limpeza")
    limpeza_pdf = models.FileField(upload_to='qsms/agregados/limpeza/', blank=True, null=True, verbose_name="Comprovante de Limpeza (PDF)")
    
    responsavel_cadastro = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="agregados_cadastrados")
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['placa']
        verbose_name = "Documentação de Agregado"
        verbose_name_plural = "Documentações de Agregados"

    def __str__(self):
        return f"{self.placa} - {self.condutor}"

    @property
    def bg_color(self):
        from datetime import date, timedelta
        hoje = date.today()
        
        cor_crlv = ''
        if self.crlv_ano < hoje.year:
            cor_crlv = 'list-group-item-danger'
        else:
            cor_crlv = 'list-group-item-success'
            
        cor_dedetizacao = 'list-group-item-success'
        if self.dedetizacao_validade:
            if self.dedetizacao_validade < hoje:
                cor_dedetizacao = 'list-group-item-danger'
            elif self.dedetizacao_validade <= hoje + timedelta(days=15):
                cor_dedetizacao = 'list-group-item-warning'
        else:
            cor_dedetizacao = 'list-group-item-warning'
            
        cor_limpeza = 'list-group-item-success'
        if self.limpeza_validade:
            if self.limpeza_validade < hoje:
                cor_limpeza = 'list-group-item-danger'
            elif self.limpeza_validade <= hoje + timedelta(days=3):
                cor_limpeza = 'list-group-item-warning'
        else:
            cor_limpeza = 'list-group-item-warning'
            
        cores = [cor_crlv, cor_dedetizacao, cor_limpeza]
        if 'list-group-item-danger' in cores:
            return 'list-group-item-danger'
        elif 'list-group-item-warning' in cores:
            return 'list-group-item-warning'
        else:
            return 'list-group-item-success'

    @property
    def status_details(self):
        from datetime import date, timedelta
        hoje = date.today()
        
        # CRLV
        if self.crlv_ano < hoje.year:
            cor_crlv = 'bg-danger-subtle text-danger-emphasis'
            texto_crlv = 'Vencido'
        else:
            cor_crlv = 'bg-success-subtle text-success-emphasis'
            texto_crlv = 'OK'
            
        # Dedetizacao
        if self.dedetizacao_validade:
            if self.dedetizacao_validade < hoje:
                cor_dedetizacao = 'bg-danger-subtle text-danger-emphasis'
                texto_dedetizacao = 'Vencido'
            elif self.dedetizacao_validade <= hoje + timedelta(days=15):
                cor_dedetizacao = 'bg-warning-subtle text-warning-emphasis'
                texto_dedetizacao = 'A Vencer'
            else:
                cor_dedetizacao = 'bg-success-subtle text-success-emphasis'
                texto_dedetizacao = 'OK'
        else:
            cor_dedetizacao = 'bg-warning-subtle text-warning-emphasis'
            texto_dedetizacao = 'Faltante'
            
        # Limpeza
        if self.limpeza_validade:
            if self.limpeza_validade < hoje:
                cor_limpeza = 'bg-danger-subtle text-danger-emphasis'
                texto_limpeza = 'Vencido'
            elif self.limpeza_validade <= hoje + timedelta(days=3):
                cor_limpeza = 'bg-warning-subtle text-warning-emphasis'
                texto_limpeza = 'A Vencer'
            else:
                cor_limpeza = 'bg-success-subtle text-success-emphasis'
                texto_limpeza = 'OK'
        else:
            cor_limpeza = 'bg-warning-subtle text-warning-emphasis'
            texto_limpeza = 'Faltante'

        alertas = []
        if texto_crlv in ['Vencido', 'A Vencer', 'Faltante']:
            alertas.append(f"CRLV ({texto_crlv})")
        if texto_dedetizacao in ['Vencido', 'A Vencer', 'Faltante']:
            alertas.append(f"Dedetização ({texto_dedetizacao})")
        if texto_limpeza in ['Vencido', 'A Vencer', 'Faltante']:
            alertas.append(f"Limpeza ({texto_limpeza})")
            
        alertas_str = ", ".join(alertas) if alertas else "Tudo OK"

        return {
            'crlv': {'cor': cor_crlv, 'texto': texto_crlv},
            'dedetizacao': {'cor': cor_dedetizacao, 'texto': texto_dedetizacao},
            'limpeza': {'cor': cor_limpeza, 'texto': texto_limpeza},
            'alertas_resumo': alertas_str
        }

class AgregadoHistorico(models.Model):
    agregado = models.ForeignKey(DocumentacaoAgregado, related_name='historico', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    acao = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Histórico de Agregado"
        verbose_name_plural = "Históricos de Agregados"

    def __str__(self):
        return f"[{self.agregado.placa}] {self.acao} em {self.timestamp.strftime('%d/%m/%Y %H:%M')}"


# ===================================================================
#           MODELO DE ARQUIVOS DIVERSOS
# ===================================================================
class ArquivoDiverso(models.Model):
    titulo = models.CharField(max_length=255, verbose_name="Título")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descricao")
    arquivo_pdf = models.FileField(upload_to='arquivos_diversos/', verbose_name="Upload de Arquivo PDF")
    responsavel_cadastro = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="arquivos_diversos_cadastrados")
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['titulo']
        verbose_name = "Arquivo Diverso"
        verbose_name_plural = "Arquivos Diversos"

    def __str__(self):
        return self.titulo

# ===================================================================
#           MODELOS DE FÁRMACO
# ===================================================================
class CertificadoFarmaco(models.Model):
    certificado = models.CharField(max_length=255, verbose_name="Certificado") 
    orgao_competente = models.CharField(max_length=255, verbose_name="Órgão Competente") 
    link_orgao = models.URLField(max_length=255, blank=True, null=True, verbose_name="Link do Órgão") 
    validade = models.DateField(verbose_name="Validade") 
    arquivo_pdf = models.FileField(upload_to='farmaco/certificados_pdf/', verbose_name="Upload de Certificado PDF") 
    descricao = models.TextField(blank=True, null=True, verbose_name="Descricao") 
    responsavel_cadastro = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="certificados_farmaco_cadastrados")

    class Meta:
        ordering = ['validade']
        verbose_name = "Certificado Fármaco"
        verbose_name_plural = "Certificados Fármaco"

    def __str__(self):
        return self.certificado

class AgendaFarmaco(models.Model):
    class TipoEvento(models.TextChoices):
        TREINAMENTO = 'Treinamento', 'Treinamento'
        EVENTO = 'Evento', 'Evento'

    tipo = models.CharField(max_length=20, choices=TipoEvento.choices, default=TipoEvento.TREINAMENTO)
    assunto = models.CharField(max_length=255, verbose_name="Assunto")
    data_evento = models.DateField(verbose_name="Data do Evento")
    hora_evento = models.TimeField(verbose_name="Hora do Evento")
    detalhes = models.TextField(blank=True, null=True, verbose_name="Detalhes")
    responsavel_cadastro = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="eventos_farmaco_cadastrados")

    class Meta:
        ordering = ['data_evento', 'hora_evento']
        verbose_name = "Evento da Agenda Fármaco"
        verbose_name_plural = "Eventos da Agenda Fármaco"

    def __str__(self):
        return f"[{self.get_tipo_display()}] {self.assunto} em {self.data_evento}"

class FarmacoTarefa(models.Model):
    class Status(models.TextChoices):
        PENDENTE = 'Pendente', 'Pendente'
        INICIADA = 'Iniciada', 'Iniciada'
        FINALIZADA = 'Finalizada', 'Finalizada'

    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.PENDENTE)
    criado_em = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-criado_em']
        verbose_name = "Tarefa de Fármaco"
        verbose_name_plural = "Tarefas de Fármaco"

    def __str__(self):
        return self.titulo

class FarmacoHistoricoTarefa(models.Model):
    tarefa = models.ForeignKey(FarmacoTarefa, related_name='historico', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    acao = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['timestamp']
        verbose_name = "Histórico de Tarefa de Fármaco"
        verbose_name_plural = "Históricos de Tarefas de Fármaco"

    def __str__(self):
        return f"[Fármaco] {self.tarefa.titulo} - {self.timestamp.strftime('%d/%m/%Y %H:%M')}"

# ===================================================================
#           MODELO PROXY PARA PERMISSÕES DE ANEXOS
# ===================================================================
class ModulePermissions(models.Model):
    """Modelo proxy para criar permissões customizadas de módulos e anexos"""
    
    class Meta:
        managed = False  # Não cria tabela no banco
        default_permissions = ()  # Não cria permissões padrão
        permissions = (
            # GR - Módulo e Anexos
            ('view_gr_module', 'Pode visualizar módulo GR'),
            ('view_gr_attachments', 'Pode visualizar anexos do GR (PGRs, Rotogramas)'),
            # Security - Módulo e Anexos
            # Security - Módulo e Anexos
            ('view_security_module', 'Pode visualizar módulo Security'),
            ('view_security_attachments', 'Pode visualizar anexos do Security (Apólices, Certificados)'),
            # QSMS - Módulo e Anexos
            ('view_qsms_module', 'Pode visualizar módulo QSMS'),
            ('view_qsms_attachments', 'Pode visualizar anexos do QSMS (Certificados)'),
            # Fármaco - Módulo e Anexos
            ('view_farmaco_module', 'Pode visualizar módulo Fármaco'),
            ('view_farmaco_attachments', 'Pode visualizar anexos do Fármaco (Certificados)'),
            # Agregados - Módulo e Anexos
            ('view_agregados_module', 'Pode visualizar módulo Documentação de Agregados'),
            ('view_agregados_attachments', 'Pode visualizar anexos de Agregados'),
            # Arquivos Diversos - Módulo
            ('view_arquivosdiversos_module', 'Pode visualizar módulo Arquivos Diversos'),
            ('view_all_arquivodiverso', 'Pode visualizar todos os arquivos diversos'),
        )
        verbose_name = "Permissão de Módulo"
        verbose_name_plural = "Permissões de Módulos"
