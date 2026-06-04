from django.contrib import admin
from django.urls import path, include
from dashboard.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    path('accounts/', include('accounts.urls')),
    path('appointments/', include('appointments.urls')),
    path('medical/', include('medical_records.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('feedback/', include('feedback.urls')),
]