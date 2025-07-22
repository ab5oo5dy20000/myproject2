from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# عرض الصفحة الرئيسية
def home_view(request):
    return render(request, 'home.html')

# عرض صفحة تسجيل الدخول
def login_view(request):
    return render(request, 'core/login.html')

# عرض صفحة إنشاء حساب ومعالجة التسجيل
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone = request.POST.get('phone')  # يمكنك تخزينه لاحقاً في بروفايل خاص
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if password != confirm:
            messages.error(request, "كلمتا المرور غير متطابقتين.")
            return render(request, 'core/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم مستخدم بالفعل.")
            return render(request, 'core/register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "البريد الإلكتروني مستخدم بالفعل.")
            return render(request, 'core/register.html')

        # إنشاء المستخدم
        User.objects.create_user(username=username, email=email, password=password)

        messages.success(request, "تم إنشاء الحساب بنجاح! يمكنك تسجيل الدخول الآن.")
        return redirect('/login/')

    return render(request, 'core/register.html')
