from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_portal_view, name='student_portal'),
]