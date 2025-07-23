from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home_view, name='home'),                # ✅ الصفحة الرئيسية
    path('login/', views.login_view, name='login'),        # ✅ تسجيل الدخول
    path('register/', views.register_view, name='register'),# ✅ إنشاء حساب
    path('logout/', views.logout_view, name='logout'),     # ✅ تسجيل الخروج
]
