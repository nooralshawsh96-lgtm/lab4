from django.shortcuts import render, get_object_or_404
from .models import LabBranch

# دالة لوحة التحكم الأولى
def dashboard_view(request):
    # جلب جميع المعامل من قاعدة البيانات
    labs_list = LabBranch.objects.all()
    context = {
        'labs_list': labs_list,
    }
    return render(request, 'branches/dashboard.html', context)

# دالة تفاصيل المعمل
def lab_detail_view(request, pk):
    # جلب المعمل أو إرجاع صفحة 404 إذا لم يكن موجوداً
    lab = get_object_or_404(LabBranch, pk=pk)
    return render(request, 'branches/lab_detail.html', {'lab': lab})