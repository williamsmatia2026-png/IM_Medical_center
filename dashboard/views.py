from django.shortcuts import render
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    ...

def dashboard(request):

    total_patients = Patient.objects.count()

    total_doctors = Doctor.objects.count()

    total_appointments = Appointment.objects.count()

    pending_appointments = Appointment.objects.filter(
        status='Pending'
    ).count()

    approved_appointments = Appointment.objects.filter(
        status='Approved'
    ).count()

    recent_appointments = Appointment.objects.order_by(
        '-id'
    )[:5]

    context = {
        'total_patients': total_patients,
        'total_doctors': total_doctors,
        'total_appointments': total_appointments,
        'pending_appointments': pending_appointments,
        'approved_appointments': approved_appointments,
        'recent_appointments': recent_appointments,
    }

    return render(
        request,
        'dashboard/dashboard.html',
        context
    )
def home(request):

    return render(
        request,
        'home.html'
    )
# Create your views here.
