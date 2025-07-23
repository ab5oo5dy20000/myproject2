import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject2.settings")
django.setup()

from django.core.mail import send_mail

try:
    result = send_mail(
        subject='اختبار من Django',
        message='هل وصلتك هذه الرسالة؟',
        from_email='ab5oo5dy20000@gmail.com',
        recipient_list=['ab5oo5dy20000@gmail.com'],
        fail_silently=False,
    )
    print(f"تم الإرسال؟ ✅ result = {result}")
except Exception as e:
    print(f"❌ حدث خطأ أثناء الإرسال: {e}")
