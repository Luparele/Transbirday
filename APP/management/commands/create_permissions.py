from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from APP.models import (
    PGR, Checklist, Rotograma, Tarefa, CondutorBlacklist,
    Seguro, Sinistro, VeiculoAssegurado, SecurityTarefa,
    CertificadoQSMS, AgendaQSMS, QsmsTarefa,
    CertificadoFarmaco, AgendaFarmaco, FarmacoTarefa,
    ArquivoDiverso
)

class Command(BaseCommand):
    help = 'Cria permissões customizadas para o sistema'

    def handle(self, *args, **kwargs):
        self.stdout.write('Criando permissões customizadas...')
        
        # Estrutura: (model, codename, name)
        permissions = [
            # GERENCIAMENTO DE RISCO
            (PGR, 'view_gr_module', 'Pode visualizar módulo Gerenciamento de Risco'),
            (PGR, 'add_pgr', 'Pode adicionar PGR'),
            (PGR, 'change_pgr', 'Pode editar PGR'),
            (PGR, 'delete_pgr', 'Pode excluir PGR'),
            
            (Checklist, 'add_checklist', 'Pode adicionar Checklist'),
            (Checklist, 'change_checklist', 'Pode editar Checklist'),
            (Checklist, 'delete_checklist', 'Pode excluir Checklist'),
            
            (Rotograma, 'add_rotograma', 'Pode adicionar Rotograma'),
            (Rotograma, 'change_rotograma', 'Pode editar Rotograma'),
            (Rotograma, 'delete_rotograma', 'Pode excluir Rotograma'),
            
            (Tarefa, 'add_tarefa', 'Pode adicionar Tarefa GR'),
            (Tarefa, 'change_tarefa', 'Pode editar Tarefa GR'),
            (Tarefa, 'delete_tarefa', 'Pode excluir Tarefa GR'),
            
            (CondutorBlacklist, 'add_condutorblacklist', 'Pode adicionar Black List'),
            (CondutorBlacklist, 'change_condutorblacklist', 'Pode editar Black List'),
            (CondutorBlacklist, 'delete_condutorblacklist', 'Pode excluir Black List'),
            
            # SECURITY
            (Seguro, 'view_security_module', 'Pode visualizar módulo Security'),
            (Seguro, 'add_seguro', 'Pode adicionar Seguro'),
            (Seguro, 'change_seguro', 'Pode editar Seguro'),
            (Seguro, 'delete_seguro', 'Pode excluir Seguro'),
            
            (Sinistro, 'add_sinistro', 'Pode adicionar Sinistro'),
            (Sinistro, 'change_sinistro', 'Pode editar Sinistro'),
            (Sinistro, 'delete_sinistro', 'Pode excluir Sinistro'),
            
            (VeiculoAssegurado, 'add_veiculoassegurado', 'Pode adicionar Veículo Assegurado'),
            (VeiculoAssegurado, 'change_veiculoassegurado', 'Pode editar Veículo Assegurado'),
            (VeiculoAssegurado, 'delete_veiculoassegurado', 'Pode excluir Veículo Assegurado'),
            
            (SecurityTarefa, 'add_securitytarefa', 'Pode adicionar Tarefa Security'),
            (SecurityTarefa, 'change_securitytarefa', 'Pode editar Tarefa Security'),
            (SecurityTarefa, 'delete_securitytarefa', 'Pode excluir Tarefa Security'),
            
            # QSMS
            (CertificadoQSMS, 'view_qsms_module', 'Pode visualizar módulo QSMS'),
            (CertificadoQSMS, 'add_certificadoqsms', 'Pode adicionar Certificado QSMS'),
            (CertificadoQSMS, 'change_certificadoqsms', 'Pode editar Certificado QSMS'),
            (CertificadoQSMS, 'delete_certificadoqsms', 'Pode excluir Certificado QSMS'),
            
            (AgendaQSMS, 'add_agendaqsms', 'Pode adicionar Agenda QSMS'),
            (AgendaQSMS, 'change_agendaqsms', 'Pode editar Agenda QSMS'),
            (AgendaQSMS, 'delete_agendaqsms', 'Pode excluir Agenda QSMS'),
            
            (QsmsTarefa, 'add_qsmstarefa', 'Pode adicionar Tarefa QSMS'),
            (QsmsTarefa, 'change_qsmstarefa', 'Pode editar Tarefa QSMS'),
            (QsmsTarefa, 'delete_qsmstarefa', 'Pode excluir Tarefa QSMS'),
            
            # FÁRMACO
            (CertificadoFarmaco, 'view_farmaco_module', 'Pode visualizar módulo Fármaco'),
            (CertificadoFarmaco, 'add_certificadofarmaco', 'Pode adicionar Certificado Fármaco'),
            (CertificadoFarmaco, 'change_certificadofarmaco', 'Pode editar Certificado Fármaco'),
            (CertificadoFarmaco, 'delete_certificadofarmaco', 'Pode excluir Certificado Fármaco'),
            
            (AgendaFarmaco, 'add_agendafarmaco', 'Pode adicionar Agenda Fármaco'),
            (AgendaFarmaco, 'change_agendafarmaco', 'Pode editar Agenda Fármaco'),
            (AgendaFarmaco, 'delete_agendafarmaco', 'Pode excluir Agenda Fármaco'),
            
            (FarmacoTarefa, 'add_farmacotarefa', 'Pode adicionar Tarefa Fármaco'),
            (FarmacoTarefa, 'change_farmacotarefa', 'Pode editar Tarefa Fármaco'),
            (FarmacoTarefa, 'delete_farmacotarefa', 'Pode excluir Tarefa Fármaco'),
            
            # ARQUIVOS DIVERSOS
            (ArquivoDiverso, 'view_arquivosdiversos_module', 'Pode visualizar Arquivos Diversos'),
            (ArquivoDiverso, 'view_all_arquivodiverso', 'Pode visualizar todos os Arquivos Diversos'),
        ]
        
        created_count = 0
        for model, codename, name in permissions:
            content_type = ContentType.objects.get_for_model(model)
            permission, created = Permission.objects.get_or_create(
                codename=codename,
                content_type=content_type,
                defaults={'name': name}
            )
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'✓ Criada: {name}'))
            else:
                self.stdout.write(f'  Já existe: {name}')
        
        self.stdout.write(self.style.SUCCESS(f'\n✅ Total: {created_count} permissões criadas'))
        self.stdout.write(self.style.SUCCESS(f'📋 Total no sistema: {len(permissions)} permissões'))
