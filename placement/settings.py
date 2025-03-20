from pathlib import Path
import os
import dj_database_url
from whitenoise import WhiteNoise  # For static file handling in production

# Base directory for your project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY - Use environment variable for security (never hardcode in production)
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-p*&ro5dz-j6s2i%ea+6blvkw&)&*2ovk-&d_+v#vdp%rv_u2*i')

# DEBUG - Set to False in production for security
DEBUG = False

# ALLOWED_HOSTS - Use your Railway URL here, or your custom domain if you have one
ALLOWED_HOSTS = ['your-railway-url.onrender.com']  # Replace with your actual Railway URL

# Installed applications for Django
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise',  # Add WhiteNoise for static files handling
    'placementapps',  # Your custom app name
]

# Middleware for your Django project
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Middleware for serving static files efficiently
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL configuration for your Django project
ROOT_URLCONF = 'placement.urls'

# Template settings for Django
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application for deployment
WSGI_APPLICATION = 'placement.wsgi.application'

# Database configuration for MySQL (using environment variables)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Use MySQL for the database engine
        'NAME': os.getenv('railway'),    # MySQL database name
        'USER': os.getenv('root'),        # MySQL database user
        'PASSWORD': os.getenv('xHPXZeXQoWmThVXcBDEfzlQMutZiaqFi'),  # MySQL user password
        'HOST': os.getenv('mysql.railway.internal'),        # MySQL host (usually provided by Railway)
        'PORT': os.getenv('3306'),        # MySQL port (usually 3306)
    }
}

# Password validation settings for Django
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Localization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'  # Set to your time zone
USE_I18N = True
USE_TZ = True

# Static files settings for production (CSS, JavaScript, Images)
STATIC_URL = '/static/'  # URL path to access static files

# Path to collect static files in production (they will be served by WhiteNoise)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files settings (for handling uploaded media like images, documents, etc.)
MEDIA_URL = '/media/'  # URL path for media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Path to store media files

# WhiteNoise configuration for static file compression and caching
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default auto field for primary keys
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Security settings for production
SECURE_SSL_REDIRECT = True  # Redirect all HTTP traffic to HTTPS
CSRF_COOKIE_SECURE = True   # Ensure CSRF cookies are only sent over HTTPS
SESSION_COOKIE_SECURE = True  # Ensure session cookies are only sent over HTTPS

# Ensure the app is using HTTPS in production
SECURE_HSTS_SECONDS = 3600  # HTTP Strict Transport Security (HSTS) settings
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Content Security Policy and other headers for enhanced security
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'  # Prevent clickjacking

# Logging configuration (optional)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
