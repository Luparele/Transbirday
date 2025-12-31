from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),

    # ===================================================================
    #           ROTAS DE AUTENTICAÇÃO
    # ===================================================================
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.custom_logout_view, name='logout'),
    path('password_change/', views.CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.password_change_done_view, name='password_change_done'),

    # Rotas de PGR
    path('pgrs/', views.pgr_list_view, name='pgr_list'),
    path('pgrs/<int:pk>/update/', views.pgr_update_view, name='pgr_update'),
    path('pgrs/<int:pk>/edit-form/', views.pgr_edit_form_view, name='pgr_edit_form'),
    
    # ===================================================================
    #           INÍCIO DAS NOVAS ROTAS (BLACK LIST)
    # ===================================================================
    path('blacklist/', views.blacklist_list_view, name='blacklist_list'),
    path('blacklist/<int:pk>/update/', views.blacklist_update_view, name='blacklist_update'),
    path('blacklist/<int:pk>/edit-form/', views.blacklist_edit_form_view, name='blacklist_edit_form'),
    path('blacklist/<int:pk>/delete/', views.blacklist_delete_view, name='blacklist_delete'),
    # ===================================================================
    #                         FIM DAS ADIÇÕES
    # ===================================================================

    # Rotas de Checklist e Gerenciadoras
    path('checklists/', views.checklist_view, name='checklist_view'),
    path('gerenciadoras/create/', views.gerenciadora_create_view, name='gerenciadora_create'),
    path('gerenciadoras/<int:pk>/update/', views.gerenciadora_update_view, name='gerenciadora_update'),
    path('gerenciadoras/<int:pk>/delete/', views.gerenciadora_delete_view, name='gerenciadora_delete'),

    # Rotas de Veículos
    path('veiculos/create/', views.veiculo_create_view, name='veiculo_create'),
    path('veiculos/<int:pk>/update/', views.veiculo_update_view, name='veiculo_update'),
    path('veiculos/<int:pk>/delete/', views.veiculo_delete_view, name='veiculo_delete'),
    
    # Rotas de Checklist
    path('checklists/create/', views.checklist_create_or_update_view, name='checklist_create'),
    path('checklists/<int:pk>/update/', views.checklist_create_or_update_view, name='checklist_update'),

    # Rotas de Rotogramas
    path('rotogramas/', views.rotograma_list_view, name='rotograma_list'),
    path('rotogramas/create/', views.rotograma_create_view, name='rotograma_create'),
    path('rotogramas/<int:pk>/update/', views.rotograma_update_view, name='rotograma_update'),
    path('rotogramas/<int:pk>/delete/', views.rotograma_delete_view, name='rotograma_delete'),

    # Rotas de Tarefas de GR (Existentes)
    path('tarefas/', views.tarefa_kanban_view, name='tarefa_list'),
    path('tarefas/create/', views.tarefa_create_view, name='tarefa_create'),
    path('tarefas/<int:pk>/iniciar/', views.tarefa_iniciar_view, name='tarefa_iniciar'),
    path('tarefas/<int:pk>/finalizar/', views.tarefa_finalizar_view, name='tarefa_finalizar'),
    path('tarefas/<int:pk>/detalhes/', views.tarefa_detalhes_json, name='tarefa_detalhes_json'),
    path('tarefas/<int:pk>/adicionar_acao/', views.tarefa_adicionar_acao_view, name='tarefa_adicionar_acao'),
    
    # --- ROTAS PARA TAREFAS DE SECURITY ---
    path('security/tarefas/', views.security_tarefa_kanban_view, name='security_tarefa_list'),
    path('security/tarefas/create/', views.security_tarefa_create_view, name='security_tarefa_create'),
    path('security/tarefas/<int:pk>/iniciar/', views.security_tarefa_iniciar_view, name='security_tarefa_iniciar'),
    path('security/tarefas/<int:pk>/finalizar/', views.security_tarefa_finalizar_view, name='security_tarefa_finalizar'),
    path('security/tarefas/<int:pk>/detalhes/', views.security_tarefa_detalhes_json, name='security_tarefa_detalhes_json'),
    path('security/tarefas/<int:pk>/adicionar_acao/', views.security_tarefa_adicionar_acao_view, name='security_tarefa_adicionar_acao'),

    # Rotas de Gestão de Seguros
    path('seguros/', views.seguro_list_view, name='seguro_list'),
    path('seguros/<int:pk>/update/', views.seguro_update_view, name='seguro_update'),
    path('seguros/<int:pk>/edit-form/', views.seguro_edit_form_view, name='seguro_edit_form'),
    path('seguros/<int:pk>/delete/', views.seguro_delete_view, name='seguro_delete'),

    # Rotas de Gestão de Sinistros
    path('sinistros/', views.sinistro_list_view, name='sinistro_list'),
    path('sinistros/<int:pk>/update/', views.sinistro_update_view, name='sinistro_update'),
    path('sinistros/<int:pk>/edit-form/', views.sinistro_edit_form_view, name='sinistro_edit_form'),
    path('sinistros/<int:pk>/delete/', views.sinistro_delete_view, name='sinistro_delete'),

    # Rotas de Veículos Assegurados
    path('veiculos-assegurados/', views.veiculo_assegurado_list_view, name='veiculo_assegurado_list'),
    path('veiculos-assegurados/<int:pk>/update/', views.veiculo_assegurado_update_view, name='veiculo_assegurado_update'),
    path('veiculos-assegurados/<int:pk>/edit-form/', views.veiculo_assegurado_edit_form_view, name='veiculo_assegurado_edit_form'),
    path('veiculos-assegurados/<int:pk>/delete/', views.veiculo_assegurado_delete_view, name='veiculo_assegurado_delete'),

    # --- ROTAS DE CERTIFICADOS QSMS ---
    path('qsms/certificados/', views.certificado_qsms_list_view, name='certificado_qsms_list'),
    path('qsms/certificados/<int:pk>/update/', views.certificado_qsms_update_view, name='certificado_qsms_update'),
    path('qsms/certificados/<int:pk>/edit-form/', views.certificado_qsms_edit_form_view, name='certificado_qsms_edit_form'),
    path('qsms/certificados/<int:pk>/delete/', views.certificado_qsms_delete_view, name='certificado_qsms_delete'),

    # --- ROTAS DE AGENDA QSMS ---
    path('qsms/agenda/', views.agenda_qsms_list_view, name='agenda_qsms_list'),
    path('qsms/agenda/<int:pk>/update/', views.agenda_qsms_update_view, name='agenda_qsms_update'),
    path('qsms/agenda/<int:pk>/edit-form/', views.agenda_qsms_edit_form_view, name='agenda_qsms_edit_form'),
    path('qsms/agenda/<int:pk>/delete/', views.agenda_qsms_delete_view, name='agenda_qsms_delete'),
    
    # --- ROTAS DE TAREFAS QSMS ---
    path('qsms/tarefas/', views.qsms_tarefa_kanban_view, name='qsms_tarefa_list'),
    path('qsms/tarefas/create/', views.qsms_tarefa_create_view, name='qsms_tarefa_create'),
    path('qsms/tarefas/<int:pk>/iniciar/', views.qsms_tarefa_iniciar_view, name='qsms_tarefa_iniciar'),
    path('qsms/tarefas/<int:pk>/finalizar/', views.qsms_tarefa_finalizar_view, name='qsms_tarefa_finalizar'),
    path('qsms/tarefas/<int:pk>/detalhes/', views.qsms_tarefa_detalhes_json, name='qsms_tarefa_detalhes_json'),
    path('qsms/tarefas/<int:pk>/adicionar_acao/', views.qsms_tarefa_adicionar_acao_view, name='qsms_tarefa_adicionar_acao'),
    
    # --- ROTAS DE ARQUIVOS DIVERSOS ---
    path('arquivos-diversos/', views.arquivo_diverso_list_view, name='arquivo_diverso_list'),
    path('arquivos-diversos/<int:pk>/update/', views.arquivo_diverso_update_view, name='arquivo_diverso_update'),
    path('arquivos-diversos/<int:pk>/edit-form/', views.arquivo_diverso_edit_form_view, name='arquivo_diverso_edit_form'),
    path('arquivos-diversos/<int:pk>/delete/', views.arquivo_diverso_delete_view, name='arquivo_diverso_delete'),

    # Fármaco - Certificados
    path('farmaco/certificados/', views.certificado_farmaco_list_view, name='certificado_farmaco_list'),
    path('farmaco/certificados/<int:pk>/edit-form/', views.certificado_farmaco_edit_form_view, name='certificado_farmaco_edit_form'),
    path('farmaco/certificados/<int:pk>/update/', views.certificado_farmaco_update_view, name='certificado_farmaco_update'),
    path('farmaco/certificados/<int:pk>/delete/', views.certificado_farmaco_delete_view, name='certificado_farmaco_delete'),
    
    # Fármaco - Agenda
    path('farmaco/agenda/', views.agenda_farmaco_list_view, name='agenda_farmaco_list'),
    path('farmaco/agenda/<int:pk>/edit-form/', views.agenda_farmaco_edit_form_view, name='agenda_farmaco_edit_form'),
    path('farmaco/agenda/<int:pk>/update/', views.agenda_farmaco_update_view, name='agenda_farmaco_update'),
    path('farmaco/agenda/<int:pk>/delete/', views.agenda_farmaco_delete_view, name='agenda_farmaco_delete'),
    
    # Fármaco - Tarefas (Kanban)
    path('farmaco/tarefas/', views.farmaco_tarefa_kanban_view, name='farmaco_tarefa_list'),
    path('farmaco/tarefas/criar/', views.farmaco_tarefa_create_view, name='farmaco_tarefa_create'),
    path('farmaco/tarefas/<int:pk>/iniciar/', views.farmaco_tarefa_iniciar_view, name='farmaco_tarefa_iniciar'),
    path('farmaco/tarefas/<int:pk>/finalizar/', views.farmaco_tarefa_finalizar_view, name='farmaco_tarefa_finalizar'),
    path('farmaco/tarefas/<int:pk>/detalhes/', views.farmaco_tarefa_detalhes_json, name='farmaco_tarefa_detalhes'),
    path('farmaco/tarefas/<int:pk>/adicionar-acao/', views.farmaco_tarefa_adicionar_acao_view, name='farmaco_tarefa_adicionar_acao'),
    
    # Gerenciamento de Usuários e Permissões (apenas admin)
    path('gerenciar-usuarios/', views.manage_users_list, name='manage_users_list'),
    path('gerenciar-usuarios/novo/', views.manage_user_permissions, name='manage_user_new'),
    path('gerenciar-usuarios/<int:user_id>/editar/', views.manage_user_permissions, name='manage_user_edit'),
    path('gerenciar-usuarios/<int:user_id>/excluir/', views.delete_user, name='delete_user'),
    
    # ===================================================================
    #           ROTAS PARA DOWNLOAD DE ARQUIVOS PROTEGIDOS
    # ===================================================================
    path('pgrs/<int:pk>/arquivo/', views.serve_pgr_file, name='serve_pgr_file'),
    path('rotogramas/<int:pk>/arquivo/', views.serve_rotograma_file, name='serve_rotograma_file'),
    path('seguros/<int:pk>/apolice/', views.serve_seguro_apolice_file, name='serve_seguro_apolice_file'),
    path('seguros/<int:pk>/certificado/', views.serve_seguro_certificado_file, name='serve_seguro_certificado_file'),
    path('qsms/certificados/<int:pk>/arquivo/', views.serve_certificado_qsms_file, name='serve_certificado_qsms_file'),
    path('farmaco/certificados/<int:pk>/arquivo/', views.serve_certificado_farmaco_file, name='serve_certificado_farmaco_file'),
]