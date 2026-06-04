from django.db import models

class Doctor(models.Model):

    name = models.CharField(max_length=100)

    specialization = models.CharField(max_length=100)

    phone = models.CharField(max_length=20)

    email = models.EmailField()

    available_days = models.CharField(max_length=100)

    start_time = models.TimeField()

    end_time = models.TimeField()

    def __str__(self):
        return self.name
# Create your models here.
