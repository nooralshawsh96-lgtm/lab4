from django.db import models

class LabBranch(models.Model):
    # 1. بيانات التعريف الأساسية
    branch_name = models.CharField(max_length=150, verbose_name="اسم المعمل")
    branch_code = models.CharField(max_length=50, unique=True, verbose_name="كود المعمل")
    
    # 2. الموقع والوصف
    location = models.CharField(max_length=200, verbose_name="موقع المعمل (مثل: مبنى أ - الدور 2)")
    description = models.TextField(verbose_name="وصف مختصر للأنشطة")
    
    # 3. الحالة الفنية (مهم جداً للإدارة)
    is_active = models.BooleanField(default=True, verbose_name="هل المعمل متاح حالياً؟")
    capacity = models.IntegerField(default=20, verbose_name="السعة الاستيعابية")
    
    # 4. صورة المعمل (اختياري)
    image = models.ImageField(upload_to='lab_images/', null=True, blank=True, verbose_name="صورة المعمل")

    def __str__(self):
        return self.branch_name
    
    class Meta:
        verbose_name = "معمل"
        verbose_name_plural = "المعامل"