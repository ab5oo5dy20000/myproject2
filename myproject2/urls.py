from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # توجيه التطبيقات الثلاثة
    path('', include('core.urls')),                # ✅ عرض صفحة تسجيل الدخول مباشرة في الصفحة الرئيسية
    path('products/', include('prodact.urls')),    # المنتجات
    path('store/', include('store.urls')),         # المتجر - أقسام أخرى
]
