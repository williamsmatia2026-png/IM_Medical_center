from django.db import models
from patients.models import Patient
from doctors.models import Doctor

class Appointment(models.Model):

    STATUS = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Cancelled', 'Cancelled'),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='Pending'
    )

    def __str__(self):
        return f"{self.patient.user.username} - {self.doctor.name}"
# Create your models here.
