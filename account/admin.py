from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    # الأعمدة التي ستظهر في جدول لوحة التحكم
    list_display = ('user', 'get_email', 'get_first_name', 'get_last_name', 'created_at') # أو الحقول الموجودة عندك
    
    # دالة لجلب البريد الإلكتروني من جدول المستخدم الأساسي
    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'البريد الإلكتروني'

    # دالة لجلب الاسم الأول من جدول المستخدم الأساسي
    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'الاسم الأول'

    # دالة لجلب الاسم الأخير من جدول المستخدم الأساسي
    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'اسم العائلة'