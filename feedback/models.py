from django.db import models
from patients.models import Patient

class Feedback(models.Model):

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )

    subject = models.CharField(max_length=100)

    message = models.TextField()

    submitted_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.subject
# Create your models here.
