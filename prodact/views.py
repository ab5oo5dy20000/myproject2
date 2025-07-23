from django.shortcuts import render
from prodact.models import Product  # تأكد أن app name = prodact

def home_view(request):
    # جلب جميع المنتجات من قاعدة البيانات
    products = Product.objects.all()

    # تمريرها إلى القالب الرئيسي للعرض
    return render(request, 'home.html', {
        'products': products
    })
