"""
Script para corrigir permissÃµes duplicadas no banco de dados
Execute com: python fix_permissions.py
"""
import os
import sys
import django

# Configurar o Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Transbirday_Project.settings')
sys.path.insert(0, '/home/Transbirday/Transbirday')
django.setup()

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Count

print("=" * 60)
print("DIAGNÃ“STICO DE PERMISSÃ•ES DUPLICADAS")
print("=" * 60)

# Encontrar permissÃµes duplicadas
duplicates = Permission.objects.values('codename').annotate(count=Count('id')).filter(count__gt=1)

if not duplicates:
    print("\nâœ… Nenhuma permissÃ£o duplicada encontrada!")
else:
    print(f"\nâš ï¸�  Encontradas {len(duplicates)} permissÃµes duplicadas:\n")
    
    for d in duplicates:
        codename = d['codename']
        perms = Permission.objects.filter(codename=codename).order_by('id')
        print(f"PermissÃ£o: {codename} ({d['count']} duplicatas)")
        
        for p in perms:
            print(f"  - ID: {p.id}, Content Type: {p.content_type.app_label}.{p.content_type.model}")
        print()

    # Perguntar se deseja corrigir
    resposta = input("\nDeseja remover as duplicatas? (s/n): ").strip().lower()
    
    if resposta == 's':
        print("\nðŸ”§ Removendo duplicatas...")
        
        for d in duplicates:
            codename = d['codename']
            perms = Permission.objects.filter(codename=codename).order_by('id')
            
            # Manter a primeira (mais antiga), remover as outras
            perms_list = list(perms)
            keep = perms_list[0]
            remove = perms_list[1:]
            
            print(f"  {codename}: mantendo ID {keep.id}, removendo {[p.id for p in remove]}")
            
            for p in remove:
                # Antes de deletar, transferir usuÃ¡rios que tÃªm essa permissÃ£o
                users_with_perm = p.user_set.all()
                for user in users_with_perm:
                    if not user.user_permissions.filter(id=keep.id).exists():
                        user.user_permissions.add(keep)
                    user.user_permissions.remove(p)
                
                # Transferir grupos tambÃ©m
                groups_with_perm = p.group_set.all()
                for group in groups_with_perm:
                    if not group.permissions.filter(id=keep.id).exists():
                        group.permissions.add(keep)
                    group.permissions.remove(p)
                
                p.delete()
        
        print("\nâœ… Duplicatas removidas com sucesso!")
    else:
        print("\nâ�Œ OperaÃ§Ã£o cancelada.")

print("\n" + "=" * 60)
print("VERIFICAÃ‡ÃƒO FINAL")
print("=" * 60)

# Verificar novamente
duplicates_after = Permission.objects.values('codename').annotate(count=Count('id')).filter(count__gt=1)
if not duplicates_after:
    print("âœ… Nenhuma permissÃ£o duplicada no banco!")
else:
    print(f"âš ï¸�  Ainda existem {len(duplicates_after)} permissÃµes duplicadas")

# Listar permissÃµes do APP
print("\n" + "=" * 60)
print("PERMISSÃ•ES DO APP ATUALMENTE")
print("=" * 60)
app_perms = Permission.objects.filter(content_type__app_label='APP').order_by('codename')
for p in app_perms:
    print(f"  {p.codename}: {p.name}")

print(f"\nTotal: {app_perms.count()} permissÃµes")
