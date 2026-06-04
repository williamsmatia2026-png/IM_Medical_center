from django.urls import path
from .views import add_record, medical_history

urlpatterns = [

    path(
        'add/',
        add_record,
        name='add_record'
    ),

    path(
        'history/',
        medical_history,
        name='medical_history'
    ),
]