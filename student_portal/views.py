from django.shortcuts import render
from .models import LabBooking

def student_dashboard(request):
    # جلب كل الحجوزات للتأكد من ظهورها
    bookings = LabBooking.objects.all()
    
    context = {
        'bookings': bookings
    }
    return render(request, 'student_portal/student_dashboard.html', context)