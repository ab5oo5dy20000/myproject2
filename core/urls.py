from django.urls import path
from . import views
app_name = 'core'  # ✅ هذا هو المطلوب

urlpatterns = [
    path('', views.home_view, name='home'),            # ✅ عرض الصفحة الرئيسية عند /
    path('login/', views.login_view, name='login'),    # ✅ تسجيل الدخول
    path('register/', views.register_view, name='register'),  # ✅ إنشاء حساب
]
