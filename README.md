# Transbirday - Sistema de Gestão de Transportes

Sistema web desenvolvido em Django para gestão de operações de transportes e logística da Transportes Birday LTDA.

## 🚀 Tecnologias

- Python 3.x
- Django 5.2.7
- SQLite
- CKEditor para edição de conteúdo
- Bleach para sanitização HTML

## 📋 Funcionalidades

- Gestão de frotas
- Controle de seguros
- Análise financeira
- Comunicação com conselho
- Sistema de precificação de fretes
- Cálculo de rotas

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/Transbirday.git
cd Transbirday
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute as migrações:
```bash
python manage.py migrate
```

5. Crie um superusuário:
```bash
python manage.py createsuperuser
```

6. Execute o servidor de desenvolvimento:
```bash
python manage.py runserver
```

## 📁 Estrutura do Projeto

```
Transbirday/
├── APP/                    # Aplicação principal
├── Transbirday_Project/    # Configurações do projeto
├── static/                 # Arquivos estáticos
├── media/                  # Upload de arquivos
├── DOCS/                   # Documentação
└── manage.py              # Script de gerenciamento Django
```

## 📄 Licença

Este projeto é de uso privado da Transportes Birday LTDA.

## 👤 Autor

Eduardo - Desenvolvimento e Manutenção
