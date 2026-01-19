"""
Configuración de producción para Huellitas
"""
import os
from pathlib import Path
from .base import *

# Para desarrollo/pruebas locales con .env 
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Debug DEBE estar en False en producción
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Hosts permitidos - Render dará la URL cuando se haga despliegue
ALLOWED_HOSTS = [
    '.onrender.com',  # Permite todos los subdominios de Render
    'localhost',
    '127.0.0.1',
]

# Agregar dominios personalizados 
if os.getenv('ALLOWED_HOSTS'):
    ALLOWED_HOSTS += os.getenv('ALLOWED_HOSTS').split(',')

# Seguridad (solo si se usa HTTPS, que Render provee automáticamente)
SECURE_SSL_REDIRECT = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# HSTS (HTTP Strict Transport Security)
if not DEBUG:
    SECURE_HSTS_SECONDS = 31536000  # 1 año
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

# Base de datos MySQL en Aiven
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
            'ssl': {
                'ca': os.getenv('DB_SSL_CA', '/etc/secrets/ca.pem'),
            }
        },
    }
}


# Cloudinary ya está configurado en base.py
# Solo asegúrar de que las variables de entorno estén en Render

# CORS - Configuración permisiva inicialmente, luego restringir
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://localhost:5173',
    'http://127.0.0.1:3000',
    'http://127.0.0.1:5173',
]

# Agregar origins de producción desde variables de entorno
if os.getenv('CORS_ALLOWED_ORIGINS'):
    CORS_ALLOWED_ORIGINS += os.getenv('CORS_ALLOWED_ORIGINS').split(',')

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# WhiteNoise para servir archivos estáticos
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Static files
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'

# Logging mejorado para producción
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[{levelname}] {asctime} {module} {process:d} {thread:d} - {message}',
            'style': '{',
        },
        'simple': {
            'format': '[{levelname}] {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'apps': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

# Configuración de archivos subidos (tamaños máximos)
DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760  # 10MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760  # 10MB

# Tiempo de sesión (opcional)
SESSION_COOKIE_AGE = 1209600  # 2 semanas en segundos
SESSION_SAVE_EVERY_REQUEST = False

# CSRF configuración
CSRF_TRUSTED_ORIGINS = []
if os.getenv('CSRF_TRUSTED_ORIGINS'):
    CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS').split(',')
else:
    # Agregar automáticamente el dominio de Render si existe
    if os.getenv('RENDER_EXTERNAL_URL'):
        CSRF_TRUSTED_ORIGINS = [os.getenv('RENDER_EXTERNAL_URL')]