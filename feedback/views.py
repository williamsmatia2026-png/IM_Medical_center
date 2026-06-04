from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import FeedbackForm
from patients.models import Patient

@login_required
def feedback_view(request):

    patient = Patient.objects.get(
        user=request.user
    )

    if request.method == 'POST':

        form = FeedbackForm(request.POST)

        if form.is_valid():

            feedback = form.save(commit=False)

            feedback.patient = patient

            feedback.save()

            return redirect('dashboard')

    else:

        form = FeedbackForm()

    return render(
        request,
        'feedback/contact.html',
        {'form': form}
    )

# Create your views here.
