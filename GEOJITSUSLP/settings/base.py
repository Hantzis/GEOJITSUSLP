"""
Django settings for GEOJITSUSLP project.

Generated by 'django-admin startproject' using Django 2.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'home',
    'search',

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',

    'modelcluster',
    'taggit',
    'corsheaders',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',

    'rest_framework',
    'rest_framework_gis',
    'webgis',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = ['http://localhost:8080', 'https://parcelas-slp.maptitude.xyz']

ROOT_URLCONF = 'GEOJITSUSLP.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'GEOJITSUSLP.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'HOST': 'localhost',
        'NAME': 'geojitsuslp',
        'USER': 'maptitude',
        'PASSWORD': 'irnA3ev8',
    }
}

"""
OSGEO_VENV = 'C:\\Anaconda3\\Library\\bin'
#OSGEO_VENV = r'C:\Anaconda3\Lib\site-packages\osgeo'
GEOS_LIBRARY_PATH = str(OSGEO_VENV + '\\geos_c.dll')
GDAL_LIBRARY_PATH = str(OSGEO_VENV + '\\gdal203.dll')
GDAL_DATA = OSGEO_VENV
PROJ_LIB = GDAL_DATA + r'\proj'
os.environ["PATH"] += os.pathsep + str(OSGEO_VENV)
"""


OSGEO_VENV = r'C:\WPy64-3810\python-3.8.1.amd64\Lib\site-packages\osgeo'
GEOS_LIBRARY_PATH = OSGEO_VENV + r'\geos_c.dll'
GDAL_LIBRARY_PATH = OSGEO_VENV + r'\gdal300.dll'
GDAL_DRIVER_PATH = OSGEO_VENV + r'\gdalplugins'
GDAL_DATA = OSGEO_VENV + r'\data'
PROJ_LIB = GDAL_DATA + r'\proj'
# PROJ_LIB = r'C:\WPy64-3810\python-3.8.1.amd64\Lib\site-packages\pyproj\proj_dir\share\proj'

# os.environ["PATH"] += os.pathsep + str(OSGEO_VENV)
# os.environ["PATH"] += os.pathsep + str(GDAL_DATA)
# os.environ["PATH"] += os.pathsep + str(PROJ_LIB)


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ]
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# Javascript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/2.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATIC_NAME = 'static'
STATIC_ROOT = os.path.join(BASE_DIR, STATIC_NAME)
STATIC_URL = f'/{STATIC_NAME}/'

MEDIA_NAME = 'media'
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_NAME)
MEDIA_URL = f'/{MEDIA_NAME}/'

# Wagtail settings

WAGTAIL_SITE_NAME = "GEOJITSUSLP"

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'http://example.com'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}