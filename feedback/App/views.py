from django.shortcuts import render, redirect
from .forms import FeedbackForm

# Create your views here.

def feedback_form(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thank_you.html')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})

# def thank_you(request):
#     return render(request, 'thank_you.html')