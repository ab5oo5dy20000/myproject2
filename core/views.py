from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from prodact.models import Product  # ✅ لعرض المنتجات في الصفحة الرئيسية

# ✅ الصفحة الرئيسية مع عرض المنتجات
def home_view(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


# ✅ صفحة تسجيل الدخول
def login_view(request):
    return render(request, 'core/login.html')


# ✅ صفحة إنشاء حساب ومعالجة التسجيل
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone = request.POST.get('phone')  # اختياري
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        # التحقق من تطابق كلمتي المرور
        if password != confirm:
            messages.error(request, "❌ كلمتا المرور غير متطابقتين.")
            return render(request, 'core/register.html')

        # التحقق من وجود اسم المستخدم مسبقًا
        if User.objects.filter(username=username).exists():
            messages.error(request, "❌ اسم المستخدم مستخدم بالفعل.")
            return render(request, 'core/register.html')

        # التحقق من وجود البريد مسبقًا
        if User.objects.filter(email=email).exists():
            messages.error(request, "❌ البريد الإلكتروني مستخدم بالفعل.")
            return render(request, 'core/register.html')

        # إنشاء المستخدم
        User.objects.create_user(username=username, email=email, password=password)

        messages.success(request, "✅ تم إنشاء الحساب بنجاح! يمكنك تسجيل الدخول الآن.")
        return redirect('core:login')  # تأكد أن هذا الاسم معرف في urls باسم login

    # عند فتح صفحة التسجيل (GET)
    return render(request, 'core/register.html')
