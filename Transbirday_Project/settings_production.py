"""
ConfiguraÃ§Ãµes de produÃ§Ã£o para PythonAnywhere
"""
from .settings import *

# SeguranÃ§a
DEBUG = False
ALLOWED_HOSTS = ['transbirday.pythonanywhere.com', 'www.transbirday.pythonanywhere.com']

# ConfiguraÃ§Ã£o de arquivos estÃ¡ticos para PythonAnywhere
STATIC_URL = '/static/'
STATIC_ROOT = '/home/Transbirday/Transbirday/staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/Transbirday/Transbirday/media'

# ConfiguraÃ§Ã£o de seguranÃ§a - AJUSTADO para PythonAnywhere free (HTTP)
# Descomente as linhas abaixo APENAS se tiver HTTPS configurado
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Garante que as sessÃµes funcionem corretamente
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_AGE = 86400  # 24 horas
