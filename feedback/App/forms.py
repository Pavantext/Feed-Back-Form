from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'name',
            'city',
            'email',
            'mobile',
            'ticket_support',
            'it_support',
            'security',
            'housekeeping',
            'facilitators',
            'archakas',
            'devotion',
            'harathi',
            'fountain',
            'prasadam',
            'visit',
            'improvement_areas',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your mobile number'}),
            
            # Dropdown converted into Radio Select for single-choice
            'ticket_support': forms.RadioSelect(choices=[
                ('Strongly Agree', 'Strongly Agree'),
                ('Agree', 'Agree'),
                ('Neutral', 'Neutral'),
                ('Disagree', 'Disagree'),
                ('Strongly Disagree', 'Strongly Disagree'),
            ]),
            'it_support': forms.RadioSelect(choices=[
                ('Strongly Agree', 'Strongly Agree'),
                ('Agree', 'Agree'),
                ('Neutral', 'Neutral'),
                ('Disagree', 'Disagree'),
                ('Strongly Disagree', 'Strongly Disagree'),
            ]),
            'security': forms.RadioSelect(choices=[
                ('Strongly Agree', 'Strongly Agree'),
                ('Agree', 'Agree'),
                ('Neutral', 'Neutral'),
                ('Disagree', 'Disagree'),
                ('Strongly Disagree', 'Strongly Disagree'),
            ]),
            'housekeeping': forms.RadioSelect(choices=[
                ('Strongly Agree', 'Strongly Agree'),
                ('Agree', 'Agree'),
                ('Neutral', 'Neutral'),
                ('Disagree', 'Disagree'),
                ('Strongly Disagree', 'Strongly Disagree'),
            ]),
            'facilitators': forms.RadioSelect(choices=[
                ('Strongly Agree', 'Strongly Agree'),
                ('Agree', 'Agree'),
                ('Neutral', 'Neutral'),
                ('Disagree', 'Disagree'),
                ('Strongly Disagree', 'Strongly Disagree'),
            ]),
            'archakas': forms.RadioSelect(choices=[
                ('Strongly Agree', 'Strongly Agree'),
                ('Agree', 'Agree'),
                ('Neutral', 'Neutral'),
                ('Disagree', 'Disagree'),
                ('Strongly Disagree', 'Strongly Disagree'),
            ]),
            'devotion': forms.RadioSelect(choices=[
                ('Strongly Agree', 'Strongly Agree'),
                ('Agree', 'Agree'),
                ('Neutral', 'Neutral'),
                ('Disagree', 'Disagree'),
                ('Strongly Disagree', 'Strongly Disagree'),
            ]),
            'harathi': forms.RadioSelect(choices=[
                ('Strongly Agree', 'Strongly Agree'),
                ('Agree', 'Agree'),
                ('Neutral', 'Neutral'),
                ('Disagree', 'Disagree'),
                ('Strongly Disagree', 'Strongly Disagree'),
            ]),
            'fountain': forms.RadioSelect(choices=[
                ('Strongly Agree', 'Strongly Agree'),
                ('Agree', 'Agree'),
                ('Neutral', 'Neutral'),
                ('Disagree', 'Disagree'),
                ('Strongly Disagree', 'Strongly Disagree'),
            ]),
            'prasadam': forms.RadioSelect(choices=[
                ('Strongly Agree', 'Strongly Agree'),
                ('Agree', 'Agree'),
                ('Neutral', 'Neutral'),
                ('Disagree', 'Disagree'),
                ('Strongly Disagree', 'Strongly Disagree'),
            ]),
            'visit': forms.RadioSelect(choices=[
                ('Strongly Agree', 'Strongly Agree'),
                ('Agree', 'Agree'),
                ('Neutral', 'Neutral'),
                ('Disagree', 'Disagree'),
                ('Strongly Disagree', 'Strongly Disagree'),
            ]),
            'improvement_areas': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Mention the areas for improvement',
                'rows': 4,
            }),
        }
