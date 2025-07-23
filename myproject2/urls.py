from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # توجيه التطبيقات
    path('', include('core.urls')),              # ✅ الصفحة الرئيسية (عرض home_view)
    path('products/', include('prodact.urls')),  # 🧴 المنتجات (من تطبيق prodact)
    path('store/', include('store.urls')),       # 🏬 الأقسام والتصنيفات (من تطبيق store)
]

# دعم رفع الصور عند التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)