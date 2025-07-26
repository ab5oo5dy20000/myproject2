"""
WSGI config for myproject2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# ✅ إعداد المتغير البيئي للإعدادات
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject2.settings')

# ✅ تحميل التطبيق
application = get_wsgi_application()

# ✅ تفعيل WhiteNoise لدعم static files في الإنتاج
from whitenoise import WhiteNoise
application = WhiteNoise(application)
