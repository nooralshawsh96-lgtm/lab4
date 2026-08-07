from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from branches.models import LabBranch

def login_view(request):
    if request.method == 'POST':
        email_input = request.POST.get('email')
        password_input = request.POST.get('password')
        
        user_obj = None
        try:
            user_obj = User.objects.get(email=email_input)
        except User.DoesNotExist:
            try:
                user_obj = User.objects.get(username=email_input)
            except User.DoesNotExist:
                user_obj = None

        if user_obj is not None:
            user = authenticate(request, username=user_obj.username, password=password_input)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
                
        return render(request, 'account/login.html', {'error': 'البريد الإلكتروني أو كلمة المرور غير صحيحة'})
        
    return render(request, 'account/login.html')
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # التأكد من عدم ترك الحقول فارغة
        if not email or not password:
            return render(request, 'account/register.html', {'error': 'الرجاء إدخال البريد الإلكتروني وكلمة المرور'})
            
        username = email
        
        # التأكد من عدم وجود المستخدم أو البريد مسبقاً في جدول User أو UserProfile
        if User.objects.filter(username=username).exists() or UserProfile.objects.filter(email=email).exists():
            return render(request, 'account/register.html', {'error': 'هذا البريد الإلكتروني مستخدم مسبقاً'})
            
        # 1. إنشاء المستخدم الأساسي
        user = User.objects.create_user(
            username=username, 
            email=email, 
            password=password, 
            first_name=first_name, 
            last_name=last_name
        )
        
        # 2. إنشاء الملف الشخصي وتمرير الـ email له أيضاً
        UserProfile.objects.create(user=user, email=email)
        
        return redirect('login') # التوجيه لصفحة تسجيل الدخول بعد النجاح
        
    return render(request, 'account/register.html')
@login_required
def dashboard_view(request):
    user_profile = None
    if request.user.is_authenticated:
        try:
            user_profile = request.user.userprofile
        except UserProfile.DoesNotExist:
            user_profile = None

    # جلب المعامل وتسميتها labs_list لتتطابق مع ملف الـ HTML الخاص بك
    labs_list = LabBranch.objects.all()

    context = {
        'user_profile': user_profile,
        'labs_list': labs_list,
    }
    return render(request, 'account/dashboard.html', context)