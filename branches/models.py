from django.db import models

class LabBranch(models.Model):
    branch_name = models.CharField(max_length=100)
    branch_code = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    capacity = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='lab_images/', blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.branch_name

class LabSpecification(models.Model):
    lab = models.ForeignKey(LabBranch, on_delete=models.CASCADE, related_name='specifications')
    spec_name = models.CharField(max_length=100, blank=True, null=True)
    spec_value = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.spec_name}: {self.spec_value}"

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=50, unique=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

class StudentProfile(models.Model):
    # علاقة من واحد إلى واحد (One-to-One) مع جدول الطالب
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.student.name}"

class Course(models.Model):
    # جدول المقررات لعمل علاقة من كثير إلى كثير (Many-to-Many) مع المعامل
    course_name = models.CharField(max_length=100)
    labs = models.ManyToManyField(LabBranch, related_name='courses')

    def __str__(self):
        return self.course_name

# جدول حجوزات الطلاب (مستقل تماماً ومرتب في البداية)
class StudentLabBooking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'قيد الانتظار'),
        ('accepted', 'مقبول'),
        ('rejected', 'مرفوض'),
    ]

    student_name = models.CharField(max_length=100, verbose_name="اسم الطالب")
    student_id = models.CharField(max_length=50, verbose_name="الرقم الجامعي")
    lab_name = models.CharField(max_length=100, verbose_name="اسم المعمل المطلوب")
    booking_date = models.DateField(verbose_name="تاريخ الحجز")
    notes = models.TextField(blank=True, null=True, verbose_name="ملاحظات إضافية")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="حالة الطلب")

    def __str__(self):
        return f"{self.student_name} - {self.status}"