from django.contrib import admin
from .models import LabBooking

@admin.register(LabBooking)
class LabBookingAdmin(admin.ModelAdmin):
    list_display = ('student', 'lab_name', 'booking_date', 'time_slot', 'created_at')
    search_fields = ('lab_name', 'student__username')