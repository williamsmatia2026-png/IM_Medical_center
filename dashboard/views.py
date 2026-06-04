from datetime import date

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment
from medical_records.models import MedicalRecord


@login_required
def dashboard(request):
    user = request.user

    if user.is_staff or user.is_superuser:
        total_patients = Patient.objects.count()
        total_doctors = Doctor.objects.count()
        total_appointments = Appointment.objects.count()
        pending_appointments = Appointment.objects.filter(status='Pending').count()
        approved_appointments = Appointment.objects.filter(status='Approved').count()
        recent_appointments = Appointment.objects.order_by('-id')[:5]

        context = {
            'total_patients': total_patients,
            'total_doctors': total_doctors,
            'total_appointments': total_appointments,
            'pending_appointments': pending_appointments,
            'approved_appointments': approved_appointments,
            'recent_appointments': recent_appointments,
        }

        return render(request, 'dashboard/dashboard.html', context)

    try:
        patient = Patient.objects.get(user=user)
    except Patient.DoesNotExist:
        return redirect('home')

    upcoming_appointments = Appointment.objects.filter(
        patient=patient,
        appointment_date__gte=date.today()
    ).order_by('appointment_date')[:5]

    medical_records_count = MedicalRecord.objects.filter(patient=patient).count()
    past_appointments_count = Appointment.objects.filter(patient=patient, appointment_date__lt=date.today()).count()

    patient_context = {
        'patient_name': patient.user.get_full_name() or patient.user.username,
        'upcoming_appointments': upcoming_appointments,
        'medical_records_count': medical_records_count,
        'past_appointments_count': past_appointments_count,
    }

    return render(request, 'dashboard/patient_dashboard.html', patient_context)


def home(request):
    return render(request, 'home.html')
# Create your views here.
