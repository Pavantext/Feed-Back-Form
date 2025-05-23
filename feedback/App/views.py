from django.shortcuts import render
from .forms import FeedbackForm
import uuid


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
        feedback_questions = {question: form[field] for question, field in FEEDBACK_QUESTIONS.items()}
        if form.is_valid():
            form_token = request.session.get('form_token')
            submitted_token = request.POST.get('form_token')
            if form_token and form_token == submitted_token:
                feedback = form.save()
                user_name = feedback.name
                request.session['user_name'] = user_name
                del request.session['form_token']
                return render(request, 'thank_you.html', {'user_name': user_name})
            else:
                form.add_error(None, "This form has submitted succesfully. You can Exit now or refresh the page.")  
        # else:
        return render(request, 'feedback_form.html',
            {'form': form,
            'form_token': request.session.get('form_token', ''),
            'feedback_questions': feedback_questions
            })

    request.session['form_token'] = str(uuid.uuid4())
    form = FeedbackForm()
    feedback_questions = {question: form[field] for question, field in FEEDBACK_QUESTIONS.items()} 
    return render(request, 'feedback_form.html', {'form': form, 'form_token': request.session['form_token'], 'feedback_questions': feedback_questions})


def thank_you(request):
    user_name = request.session.get('user_name', 'User')
    return render(request, 'thank_you.html', {'user_name': user_name})