from django.shortcuts import render, get_object_or_404, redirect
from .models import LabBranch
from .forms import LabBranchForm
from django.http import JsonResponse
from django.db.models import Q
from django.contrib import messages
from .forms import LabBranchForm, StudentBookingForm # إضافة StudentBookingForm هنا
from django.shortcuts import get_object_or_404, redirect
from .models import StudentLabBooking

def accept_booking_view(request, pk):
    booking = get_object_or_404(StudentLabBooking, pk=pk)
    booking.status = 'accepted'
    booking.save()
    return redirect('dashboard') # أو أي صفحة تعرض الطلبات
def add_lab_view(request):
    if request.method == 'POST':
        form = LabBranchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = LabBranchForm()
    
    return render(request, 'branches/add_lab.html', {'form': form})

def chatbot_response(request):
    question = request.GET.get('q', '').strip()
    answer = "عذراً، لم أفهم سؤالك. جرب البحث عن اسم المعمل."
    
    if question:
        clean_query = question.replace('معمل', '').strip()
        if not clean_query:
            clean_query = question 
            
        labs = LabBranch.objects.filter(
            Q(branch_name__icontains=clean_query) | 
            Q(description__icontains=clean_query) |
            Q(branch_code__icontains=clean_query)
        )
        
        if labs.exists():
            results = []
            for lab in labs:
                name = getattr(lab, 'branch_name', getattr(lab, 'name', 'معمل'))
                desc = getattr(lab, 'description', 'لا يوجد وصف متاح')
                code = getattr(lab, 'branch_code', '')
                
                results.append(f"🧪 <b>{name}</b> ({code})<br>📝 الوصف: {desc}<br>🟢 الحالة: متاح للحجز")
                
            answer = "وجدت المعامل التالية:<br><br>" + "<br><hr>".join(results)
        elif 'حجز' in question:
            answer = "يمكنك حجز المعمل من قسم بوابة الطالب أو الضغط على زر الحجز أدناه."
        else:
            answer = "لم أجد نتائج مطابقة، تأكد من كتابة اسم المعمل بشكل صحيح."
            
    return JsonResponse({'reply': answer})


# ==========================================
# دالة لوحة التحكم المحدثة (مضاف إليها جميع المتغيرات في الـ Context)
# ==========================================
def dashboard_view(request):
    # --- تطبيق الـ 7 دوال لـ QuerySet المطلوبة في التكليف ---
    labs_list = LabBranch.objects.all()                         # 1. جلب الكل (.all)
    active_labs = LabBranch.objects.filter(is_active=True)      # 2. تصفية (.filter)
    exclude_labs = LabBranch.objects.exclude(capacity__lt=5)    # 3. استبعاد (.exclude)
    ordered_labs = LabBranch.objects.order_by('branch_name')    # 4. ترتيب (.order_by)
    labs_count = LabBranch.objects.count()                      # 5. حساب العدد (.count)
    first_lab = LabBranch.objects.first()                       # 6. جلب الأول (.first)
    
    # 7. جلب معمل محدد أو التعامل مع عدم وجوده بأمان (.get)
    try:
        specific_lab = LabBranch.objects.get(pk=1)
    except LabBranch.DoesNotExist:
        specific_lab = None

    # --- معالجة الـ Form (GET & POST) ---
    if request.method == 'POST':
        form = LabBranchForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('dashboard_view') 
    else:
        form = LabBranchForm()

    context = {
        'labs_list': labs_list,
        'active_labs': active_labs,
        'exclude_labs': exclude_labs,      # تم إضافتها بنجاح
        'ordered_labs': ordered_labs,      # تم إضافتها بنجاح
        'labs_count': labs_count,
        'first_lab': first_lab,            # تم إضافتها بنجاح
        'specific_lab': specific_lab,      # تم إضافتها بنجاح
        'form': form, 
    }
    return render(request, 'branches/dashboard.html', context)


# دالة تفاصيل المعمل (محدثة لتدعم الـ Form والشات بوت في صفحة التفاصيل)
def lab_detail_view(request, pk):
    lab = get_object_or_404(LabBranch, pk=pk)
    
    if request.method == 'POST':
        form = LabBranchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lab_detail_view', pk=lab.pk)
    else:
        form = LabBranchForm()

    context = {
        'lab': lab,
        'form': form,
    }
    return render(request, 'branches/lab_detail.html', context)


# ==========================================
# دالة نموذج حجز الطلاب (مع المسافات البادئة الصحيحة 100%)
# ==========================================
def student_booking_view(request):
    if request.method == 'POST':
        form = StudentBookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم إرسال طلبك بنجاح وحفظه في قاعدة البيانات!')
            return redirect('student_booking')
    else:
        form = StudentBookingForm()
        
    return render(request, 'branches/student_form.html', {'form': form})