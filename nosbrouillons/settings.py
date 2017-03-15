"""
Django settings for nosbrouillons project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '))^q$1y3d8=33q_bciqi4s4_#*=!-+8c_b7fxh2s*8e=n%7fbc'

PROD = False

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not PROD

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'tinymce',
    'django.contrib.staticfiles',
    'main',
    # 'news',
    'contact',
    'aboutus',
    'account',
    'work',
    'contribute',
    'django_gravatar',
    'xmpp',
    'conversejs'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nosbrouillons.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Need to specify the base templaes dir
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'nosbrouillons.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

# STATIC_URL = '/static/'
# MEDIA_URL = '/media/'

# STATICFILES_DIRS = [
#     # Need to specify the base static dir, outside the apps
#     os.path.join(BASE_DIR, "static/"),

# ]

# # MEDIAFILES_DIRS = [ #Created for a test
# #     # Need to specify the base static dir, outside the apps
# #     os.path.join(BASE_DIR, "media"),

# # ]

# # TINYMCE_JS_ROOT = os.path.join(BASE_DIR, "static/tiny_mce")
# # TINYMCE_JS_URL = os.path.join(TINYMCE_JS_ROOT, "tiny_mce.js")

# STATIC_ROOT = os.path.join(BASE_DIR, "static/")
# MEDIA_ROOT = os.path.join(BASE_DIR, "media/")


STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Pompe sur getstarted, pour test.
STATIC_ROOT = "/static/" # os.path.join(BASE_DIR, "assets/static/")

MEDIA_ROOT = os.path.join(BASE_DIR, "assets/media/")

MEDIA_URL = '/assets/media/'


### CONVERSE PART ###

XMPP_DOMAIN = 'nosbrouillons.com'if PROD else 'localhost:5050'
XMPP_BOSH_SERVICE_URL = 'https://xmpp.nosbrouillons.com:5280/http-bind' if PROD else 'localhost:5050'

# Optionally setup ConverseJS to suit your needs:

XMPP_CONVERSEJS_SETTINGS = {
    'allow_contact_removal': False,
    'allow_contact_requests': True,
    'auto_subscribe': True,
    'allow_logout': False,
    'allow_muc': True,
    'allow_otr': False,
    'allow_registration': False,
    'message_carbons': True,
    'hide_muc_server': True,
    'use_vcards': True,
    'animate': True,
    'play_sounds': True,
    'xhr_user_search': True,
    'sounds_path': '%ssounds/' % STATIC_URL,
    'visible_toolbar_buttons': {
         'call': False,
         'clear': False,
         'emoticons': True,
         'toggle_participants': False,
    }
}

XMPP_ENABLED = True
CONVERSEJS_BOSH_SERVICE_URL = 'https://my-bosh-service.com'
CONVERSEJS_AUTO_REGISTER = 'xmpp.nosbrouillons.com'


### END OF PART ###
