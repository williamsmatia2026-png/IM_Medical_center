from django.db import models
from patients.models import Patient
from doctors.models import Doctor

class MedicalRecord(models.Model):

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE
    )

    diagnosis = models.TextField()

    treatment = models.TextField()

    prescription = models.TextField()

    visit_date = models.DateField()

    def __str__(self):
        return f"{self.patient.user.username} - {self.visit_date}"
# Create your models here.
