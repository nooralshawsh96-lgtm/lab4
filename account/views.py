from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile

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
        
        if not email or not password:
            return render(request, 'account/register.html', {'error': 'الرجاء إدخال البريد الإلكتروني وكلمة المرور'})
            
        username = email
        
        if User.objects.filter(username=username).exists() or UserProfile.objects.filter(email=email).exists():
            return render(request, 'account/register.html', {'error': 'هذا البريد الإلكتروني مستخدم مسبقاً'})
            
        user = User.objects.create_user(
            username=username, 
            email=email, 
            password=password, 
            first_name=first_name, 
            last_name=last_name
        )
        
        UserProfile.objects.create(user=user, email=email)
        
        return redirect('login')
        
    return render(request, 'account/register.html')
@login_required
def dashboard_view(request):
    from branches.models import LabBranch  # <-- تم إضافة الاستيراد هنا لضمان عمله 100%
    
    user_profile = None
    if request.user.is_authenticated:
        try:
            user_profile = request.user.userprofile
        except UserProfile.DoesNotExist:
            user_profile = None

    # دوال الـ QuerySet المطلوبة للتكليف وعرضها في الداشبورد:
    labs_list = LabBranch.objects.all()                      # 1. كل المعامل
    active_labs = LabBranch.objects.filter(is_active=True)    # 2. المعامل النشطة
    exclude_labs = LabBranch.objects.exclude(capacity__lt=5)  # 3. المعامل المستبعدة
    labs_count = LabBranch.objects.count()                    # 4. العداد الكلي
    first_lab = LabBranch.objects.first()                     # 5. أول معمل مسجل
    specific_lab = LabBranch.objects.filter(pk=1).first()     # 6. معمل معين (رقم 1)

    context = {
        'user_profile': user_profile,
        'labs_list': labs_list,
        'active_labs': active_labs,
        'exclude_labs': exclude_labs,
        'labs_count': labs_count,
        'first_lab': first_lab,
        'specific_lab': specific_lab,
    }
    return render(request, 'account/dashboard.html', context)