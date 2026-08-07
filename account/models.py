from django.db import models
from django.contrib.auth.models import User # استيراد نظام المستخدمين الأساسي

class UserProfile(models.Model):
    # ربط هذا البروفايل بحساب المستخدم الأساسي (علاقة واحد لواحد)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="المستخدم")
    
    # البيانات الإضافية التي طلبتِها
    email = models.EmailField(unique=True, verbose_name="البريد الإلكتروني")
    first_name = models.CharField(max_length=50, verbose_name="الاسم الأول")
    last_name = models.CharField(max_length=50, verbose_name="اسم العائلة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ التسجيل")

    def __str__(self):
        return self.user.username # سيعرض اسم المستخدم المسجل في نظام ديجانجو