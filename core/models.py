from django.db import models
from django.contrib.auth.models import User

# ✅ استيراد الإشارات وإعدادات البريد
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings


# ✅ موديل رسائل التواصل
class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="الاسم")
    email = models.EmailField(verbose_name="البريد الإلكتروني")
    message = models.TextField(verbose_name="الرسالة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإرسال")

    class Meta:
        verbose_name = "رسالة تواصل"
        verbose_name_plural = "رسائل التواصل"

    def __str__(self):
        return f"رسالة من {self.name}"


# ✅ إرسال بريد ترحيبي عند إنشاء مستخدم جديد
@receiver(post_save, sender=User)
def send_login_success_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject='تم تسجيل دخولك بنجاح',
            message=f'مرحبًا {instance.username}، تم تسجيل دخولك إلى منصتنا بنجاح!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[instance.email],
            fail_silently=False,
        )
