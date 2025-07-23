# prodact/urls.py

from django.urls import path
from . import views  # لتضمين العروض من views.py داخل هذا التطبيق

app_name = 'prodact'

urlpatterns = [
    # مثال على صفحة عرض جميع المنتجات (يمكنك تعديل الاسم لاحقًا):
    # path('', views.product_list, name='product_list'),
]
