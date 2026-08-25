from django.contrib import admin
from django.urls import path, include
from account.views import login_view, register, dashboard_view
from branches.views import lab_detail_view, chatbot_response, student_booking_view  # تم إضافة دالة الفورم هنا
from django.conf import settings
from django.conf.urls.static import static
from branches import views as branch_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'), 
    path('register/', register, name='register'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('lab/<int:pk>/', lab_detail_view, name='lab_detail'),
    
    # مسار نموذج حجز الطلاب الجديد
    path('student-booking/', student_booking_view, name='student_booking'),
    
    path('student/', include(('student_portal.urls', 'student_portal'), namespace='student_portal')),
    
    path('chatbot-api/', chatbot_response, name='chatbot_api'),
    path('branches/add/', branch_views.add_lab_view, name='add_lab'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # تم تصحيح MEDIA_URL هنا