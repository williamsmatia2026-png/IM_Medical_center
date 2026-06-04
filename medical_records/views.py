from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import MedicalRecord
from .forms import MedicalRecordForm
from patients.models import Patient


@login_required
def add_record(request):

    if request.method == 'POST':

        form = MedicalRecordForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('medical_history')

    else:
        form = MedicalRecordForm()

    return render(
        request,
        'medical_records/add_record.html',
        {'form': form}
    )


@login_required
def medical_history(request):

    try:
        patient = Patient.objects.get(user=request.user)

        records = MedicalRecord.objects.filter(
            patient=patient
        )

    except Patient.DoesNotExist:
        records = []

    return render(
        request,
        'medical_records/history.html',
        {'records': records}
    )