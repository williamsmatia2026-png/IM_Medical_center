from django.contrib.auth.models import User
from django.db import models

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=20)
    address = models.TextField()
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.user.username
# Create your models here.
