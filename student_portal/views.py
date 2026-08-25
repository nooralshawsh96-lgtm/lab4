from django.shortcuts import render
from .models import LabBooking

def student_portal_view(request):  # غيرنا الاسم هنا ليطابق الـ urls.py
    bookings = LabBooking.objects.all()
    
    context = {
        'bookings': bookings
    }
    return render(request, 'student_portal/student_dashboard.html', context)