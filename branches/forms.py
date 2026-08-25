from django import forms
from .models import LabBranch, StudentLabBooking

# 1. فورم إضافة المعمل (المخصص للوحة التحكم أو المشرف)
class LabBranchForm(forms.ModelForm):
    class Meta:
        model = LabBranch
        fields = ['branch_name', 'branch_code', 'capacity', 'description', 'is_active', 'image']
        widgets = {
            'branch_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل اسم المعمل'}),
            'branch_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل رمز المعمل'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

# 2. فورم حجز الطلاب (الذي كتبتيه للتو)
class StudentBookingForm(forms.ModelForm):
    class Meta:
        model = StudentLabBooking
        fields = ['student_name', 'student_id', 'lab_name', 'booking_date', 'notes']
        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل اسمك الكامل'}),
            'student_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل رقمك الجامعي'}),
            'lab_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم المعمل'}),
            'booking_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'أي ملاحظات...'}),
        }