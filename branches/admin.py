from django.contrib import admin
from .models import LabBranch, LabSpecification, Student, StudentProfile, Course, StudentLabBooking  # 1. أضيفي اسم الموديل هنا

@admin.register(LabBranch)
class LabBranchAdmin(admin.ModelAdmin):
    list_display = ('branch_name', 'branch_code', 'capacity')
    search_fields = ('branch_name',)
    list_filter = ('is_active',)

@admin.register(StudentLabBooking)
class StudentLabBookingAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'student_id', 'lab_name', 'booking_date', 'status')
    list_filter = ('status', 'booking_date')
    search_fields = ('student_name', 'student_id', 'lab_name')

admin.site.register(LabSpecification)
admin.site.register(Student)
admin.site.register(StudentProfile)  # 2. تسجيل جدول البروفايل
admin.site.register(Course)         # 3. تسجيل جدول المقررات