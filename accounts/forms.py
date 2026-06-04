from django import forms
from django.contrib.auth.models import User
from patients.models import Patient

class PatientRegistrationForm(forms.ModelForm):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    class Meta:
        model = Patient
        fields = ['phone', 'address', 'gender', 'date_of_birth']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email']
        )

        patient = super().save(commit=False)
        patient.user = user

        if commit:
            patient.save()

        return patient