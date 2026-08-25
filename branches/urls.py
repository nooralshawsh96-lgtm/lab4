from django.urls import path
from . import views

urlpatterns = [
    # مسار لوحة التحكم الرئيسية
    path('', views.dashboard_view, name='dashboard'),
    path('dashboard/', views.dashboard_view, name='dashboard_view'),
    
    # مسار إضافة معمل جديد
    path('add-lab/', views.add_lab_view, name='add_lab'),
    
    # مسار تفاصيل المعمل باستخدام الرقم التعريفي (pk)
    path('lab/<int:pk>/', views.lab_detail_view, name='lab_detail'),
    
    # مسار الشات بوت التفاعلي
    path('chatbot-api/', views.chatbot_response, name='chatbot_api'),
    
    # مسار نموذج حجز الطلاب الجديد
    path('student-booking/', views.student_booking_view, name='student_booking'),
    path('booking/accept/<int:pk>/', views.accept_booking_view, name='accept_booking'),
]