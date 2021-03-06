"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

# 默认的配置在global-settings，源代码，不要去修改
from django.conf import global_settings

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8@7r2^n1hrhy9@4)wxjandrpl30+mxc0)q*^)1dj#tdvust1ia'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
    'course',
    'uploads',
    'HTML',
    'users',
    'hello',
    'books',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_db',
        'HOST': '192.168.8.130',
        'USER': 'root',
        'PASSWORD': 'DevOps@2020',
        'PORT': 3306,
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

# admin后台支持中文
LANGUAGE_CODE = 'zh-hans'
# 改为使用中国时区
TIME_ZONE = 'Asia/Shanghai'

# 开启国际化，多语言支持
USE_I18N = True
# 本地化
USE_L10N = True
# 使用时区
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    (BASE_DIR / 'static'),
)

# 全局声明，使用UserProfile
AUTH_USER_MODEL = 'users.UserProfile'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#
# MEDIA_ROOT = BASE_DIR / 'media/'
# MEDIA_URL = '/media/'



# 跳转中间页
JUMP_PAGE = "jump.html"

# logging
# 创建log目录
LOG_DIR = os.path.join(BASE_DIR, "logs")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOGGING = {
    "version":1,
    "disable_existing_loggers":False,   # 禁用已经存在的logger实例
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},

    # 日志对象
    "loggers":{
        # 自定义日志对象
        "devops":{
            'level':"DEBUG",
            'handlers':['devops_file_handle'],
            'propagate': True,
        },
        # django自带日志对象，记录控制台输出的内容
        "django":{
            'level':'DEBUG',
            'handlers':['django_file_handle'],
            'propagate':True,
        },
            },

    # 处理器
    "handlers":{
        "devops_file_handle":{
            'level':'INFO',
            'class':'logging.FileHandler',
            'filename': BASE_DIR / 'logs' / 'devops.log',
            'formatter':'devops'
        },
        "django_file_handle": {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',    # 滚动生成日志，切割
            'filename': BASE_DIR / 'logs' / 'django.log',   # 日志文件名
            'maxBytes':1024 * 1024 * 10, # 单个日志文件最大为10M
            'backupCount':5,    # 日志备份文件最大数量
            'formatter': 'devops',
            'encoding':'utf-8',
        },
                },

    # 日志格式
    "formatters": {
        'devops':{
            'format':"[%(asctime)s] [%(process)d]] [%(thread)d] [%(filename)16s:%(lineno)4d] [%(levelname)-6s] %(message)s"
        },
        "simple": {
            'format': '%(asctime)s %(levelname)s %(message)s'
        }
    },
}