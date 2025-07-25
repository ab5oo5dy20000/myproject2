from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # لوحة تحكم المشرف
    path('admin/', admin.site.urls),

    # توجيه التطبيقات الداخلية
    path('', include('core.urls')),              # 🏠 الصفحة الرئيسية
    path('products/', include('prodact.urls')),  # 🧴 المنتجات
    path('store/', include('store.urls')),       # 🏬 التصنيفات أو المتجر
]

# 🟢 دعم عرض الصور والملفات الثابتة في بيئة التطوير فقط
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
