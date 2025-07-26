from pathlib import Path
import os
import environ
import cloudinary

# المسار الجذري للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# تحميل متغيرات البيئة من ملف .env
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# إعدادات الأمان
SECRET_KEY = env('SECRET_KEY', default='django-insecure-key')
DEBUG = env.bool('DEBUG', default=True)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

# التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # تطبيقات المشروع
    'store.apps.StoreConfig',
    'prodact.apps.ProdactConfig',
    'core.apps.CoreConfig',

    # Cloudinary
    'cloudinary_storage',
    'cloudinary',
]

# الوسيطات (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ✅ دعم whitenoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# إعدادات الروابط
ROOT_URLCONF = 'myproject2.urls'

# إعدادات القوالب
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# تطبيق WSGI
WSGI_APPLICATION = 'myproject2.wsgi.application'

# قاعدة البيانات: PostgreSQL في الإنتاج، SQLite في التطوير
DATABASES = {
    'default': env.db_url(
        'DATABASE_URL',
        default=f'sqlite:///{os.path.join(BASE_DIR, "db.sqlite3")}'
    )
}

# تحقق كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# اللغة والتوقيت
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True

# الملفات الثابتة
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# ✅ دعم تخزين ملفات static للإنتاج
if not DEBUG:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ✅ إعداد Cloudinary
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': env('CLOUDINARY_API_KEY'),
    'API_SECRET': env('CLOUDINARY_API_SECRET'),
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# ✅ تهيئة Cloudinary
cloudinary.config(
    cloud_name = env('CLOUDINARY_CLOUD_NAME'),
    api_key = env('CLOUDINARY_API_KEY'),
    api_secret = env('CLOUDINARY_API_SECRET'),
    secure = True
)

# ✅ إعدادات البريد الإلكتروني (Gmail)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

# إعداد النوع الافتراضي للمفاتيح
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
