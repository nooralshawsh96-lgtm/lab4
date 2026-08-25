from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_role', 'get_email', 'get_first_name', 'get_last_name', 'created_at')
    
    # دالة لتحديد اللقب تلقائياً بناءً على صلاحيات الحساب
    def get_role(self, obj):
        if obj.user.is_superuser or obj.user.is_staff:
            return "👑 مدير النظام (Admin)"
        return "👤 مستخدم عادية"
    get_role.short_description = 'صلاحية الحساب'

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'البريد الإلكتروني'

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'الاسم الأول'

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'اسم العائلة'