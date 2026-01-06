"""
Script para corrigir encoding dos dados no banco de dados
Execute com: python fix_encoding.py
"""
import os
import sys
import django

# Configurar o Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Transbirday_Project.settings')
sys.path.insert(0, '/home/Transbirday/Transbirday')
django.setup()

from APP.models import Veiculo, Checklist

print("=" * 60)
print("CORRECAO DE ENCODING NO BANCO DE DADOS")
print("=" * 60)

# Corrigir Veiculos - padronizar para "Cavalo Mecanico" (sem acento)
print("\nVerificando Veiculos...")
veiculos = Veiculo.objects.all()
veiculos_corrigidos = 0

for veiculo in veiculos:
    tipo_original = veiculo.tipo
    novo_tipo = None
    
    # Qualquer variacao de "Cavalo Mec*nico" vira "Cavalo Mecanico"
    if 'Cavalo' in veiculo.tipo and 'Mec' in veiculo.tipo:
        novo_tipo = 'Cavalo Mecanico'
    
    if novo_tipo and novo_tipo != tipo_original:
        veiculo.tipo = novo_tipo
        veiculo.save()
        veiculos_corrigidos += 1
        print(f"  Veiculo {veiculo.placa}: '{tipo_original}' -> '{novo_tipo}'")

print(f"\nTotal de veiculos corrigidos: {veiculos_corrigidos}")

# Corrigir Checklists - padronizar "Nao" 
print("\nVerificando Checklists...")
checklists = Checklist.objects.all()
checklists_corrigidos = 0

for checklist in checklists:
    aprovado_original = checklist.aprovado
    novo_aprovado = None
    
    # Qualquer variacao de "N*o" vira "Nao"
    if checklist.aprovado and 'N' in checklist.aprovado and 'o' in checklist.aprovado.lower():
        if checklist.aprovado != 'Nao' and checklist.aprovado != 'Sim':
            novo_aprovado = 'Nao'
    
    if novo_aprovado and novo_aprovado != aprovado_original:
        checklist.aprovado = novo_aprovado
        checklist.save()
        checklists_corrigidos += 1
        print(f"  Checklist {checklist.id}: '{aprovado_original}' -> '{novo_aprovado}'")

print(f"\nTotal de checklists corrigidos: {checklists_corrigidos}")

# Mostrar dados atuais
print("\n" + "=" * 60)
print("DADOS ATUAIS NO BANCO")
print("=" * 60)

print("\nTipos de Veiculos unicos:")
tipos = Veiculo.objects.values_list('tipo', flat=True).distinct()
for t in tipos:
    count = Veiculo.objects.filter(tipo=t).count()
    print(f"  - '{t}': {count} veiculos")

print("\nStatus de Aprovacao unicos (Checklist):")
aprovados = Checklist.objects.values_list('aprovado', flat=True).distinct()
for a in aprovados:
    count = Checklist.objects.filter(aprovado=a).count()
    print(f"  - '{a}': {count} checklists")

print("\nTotal de registros:")
print(f"  - Veiculos: {Veiculo.objects.count()}")
print(f"  - Checklists: {Checklist.objects.count()}")

print("\nCorrecao concluida!")