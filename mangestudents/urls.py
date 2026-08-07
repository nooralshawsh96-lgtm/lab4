from django.contrib import admin
from account.views import login_view, register, dashboard_view
from branches.views import lab_detail_view
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('register/', register, name='register'),     # صفحة إنشاء حساب
    path('dashboard/', dashboard_view, name='dashboard'),  # لوحة التحكم
    path('lab/<int:pk>/', lab_detail_view, name='lab_detail'), # صفحة تفاصيل المعمل
    path('student/', include('student_portal.urls')),  #
]

# تفعيل عرض الصور والملفات المرفوعة في وضع التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)