from django.db import models
from django.contrib.auth.models import User

class LabBooking(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="الطالب")
    lab_name = models.CharField(max_length=100, verbose_name="اسم المعمل")
    booking_date = models.DateField(verbose_name="تاريخ الحجز")
    time_slot = models.CharField(max_length=50, verbose_name="وقت الجلسة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="وقت الطلب")

    def __str__(self):
        return f"{self.student.username} - {self.lab_name}"