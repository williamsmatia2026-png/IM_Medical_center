from django.urls import path
from .views import (book_appointment, appointment_list, doctor_schedule,approve_appointment,cancel_appointment)

urlpatterns = [
    path('book/', book_appointment, name='book_appointment'),
    path('list/', appointment_list, name='appointment_list'),
    path('doctors/', doctor_schedule, name='doctor_schedule'),
    path('approve/<int:appointment_id>/',approve_appointment,name='approve_appointment'),
    path('cancel/<int:appointment_id>/',cancel_appointment,name='cancel_appointment'),
]