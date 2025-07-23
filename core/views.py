from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from prodact.models import Product


# ✅ الصفحة الرئيسية
def home_view(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


# ✅ تسجيل الدخول
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user_auth = authenticate(request, username=user.username, password=password)

            if user_auth is not None:
                login(request, user_auth)
                messages.success(request, "✅ تم تسجيل الدخول بنجاح.")
                return redirect('core:home')
            else:
                messages.error(request, "❌ كلمة المرور غير صحيحة.")
        except User.DoesNotExist:
            messages.error(request, "❌ البريد الإلكتروني غير موجود.")

    return render(request, 'core/login.html')


# ✅ إنشاء حساب جديد
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone = request.POST.get('phone')  # ❗موجود ولكن غير محفوظ حاليًا
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if password != confirm:
            messages.error(request, "❌ كلمتا المرور غير متطابقتين.")
            return render(request, 'core/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "❌ اسم المستخدم مستخدم بالفعل.")
            return render(request, 'core/register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "❌ البريد الإلكتروني مستخدم بالفعل.")
            return render(request, 'core/register.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_staff = True  # يظهر في لوحة الأدمن
        user.save()

        login(request, user)
        return render(request, 'core/welcome.html', {'username': username})

    return render(request, 'core/register.html')


# ✅ تسجيل الخروج
def logout_view(request):
    logout(request)
    messages.info(request, "📤 تم تسجيل الخروج بنجاح.")
    return redirect('core:home')
