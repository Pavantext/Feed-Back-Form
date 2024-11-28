# from django.shortcuts import render, redirect
# from .forms import FeedbackForm

# # Create your views here.

# def feedback_form(request):
#     if request.method == "POST":
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'thank_you.html')
#     else:
#         form = FeedbackForm()
#     return render(request, 'feedback_form.html', {'form': form})

# # def thank_you(request):
# #     return render(request, 'thank_you.html')

from django.shortcuts import render, redirect
from .forms import FeedbackForm




FEEDBACK_QUESTIONS = {
    "Ticket Counter team provided excellent support and assistance.": "ticket_support",
    "IT team provided excellent support and assistance.": "it_support",
    "The security team provided excellent support and assistance.": "security",
    "The housekeeping team maintained the premises in an exceptionally clean condition.": "housekeeping",
    "The facilitators were welcoming and provided outstanding guidance.": "facilitators",
    "The Archakas guided us expertly.": "archakas",
    "I felt a deep sense of devotion.": "devotion",
    "I thoroughly enjoyed watching the 'Samatha Neerajanam (Harathi)'.": "harathi",
    "The fountain and laser show were amazing.": "fountain",
    "The prasadam is delicious and hygienic.": "prasadam",
    "I would love to visit the Statue of Equality repeatedly.": "visit",
}



def feedback_form(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thank_you.html')
    else:
        form = FeedbackForm()
    feedback_questions = {question: form[field] for question, field in FEEDBACK_QUESTIONS.items()}
    return render(request, 'feedback_form.html', {'form': form, 'feedback_questions': feedback_questions})


def thank_you(request):
    return render(request, 'thank_you.html')