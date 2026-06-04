from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from patients.models import Patient
from doctors.models import Doctor
from .models import Appointment
from .forms import AppointmentForm


# =========================
# BOOK APPOINTMENT
# =========================
@login_required
def book_appointment(request):

    try:
        patient = Patient.objects.get(user=request.user)
    except Patient.DoesNotExist:
        messages.error(request, "Patient profile not found.")
        return redirect('appointment_list')

    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = patient
            appointment.status = 'Pending'
            appointment.save()

            messages.success(request, "Appointment booked successfully.")
            return redirect('appointment_list')

    else:
        form = AppointmentForm()

    return render(request, 'appointments/book.html', {'form': form})


# =========================
# APPOINTMENT LIST
# =========================
@login_required
def appointment_list(request):

    try:
        patient = Patient.objects.get(user=request.user)
        appointments = Appointment.objects.filter(patient=patient)
    except Patient.DoesNotExist:
        appointments = []

    return render(
        request,
        'appointments/list.html',
        {'appointments': appointments}
    )


# =========================
# DOCTOR SCHEDULE
# =========================
@login_required
def doctor_schedule(request):

    search = request.GET.get('search')
    doctors = Doctor.objects.all()

    if search:
        doctors = doctors.filter(
            specialization__icontains=search
        )

    return render(
        request,
        'appointments/doctor_schedule.html',
        {'doctors': doctors}
    )


# =========================
# APPROVE APPOINTMENT
# =========================
@login_required
def approve_appointment(request, appointment_id):

    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.status = "Approved"
    appointment.save()

    return redirect('dashboard')


# =========================
# CANCEL APPOINTMENT
# =========================
@login_required
def cancel_appointment(request, appointment_id):

    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.status = "Cancelled"
    appointment.save()

    return redirect('dashboard')