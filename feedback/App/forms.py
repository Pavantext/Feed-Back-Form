# from django import forms
# from .models import Feedback

# class FeedbackForm(forms.ModelForm):
#     class Meta:
#         model = Feedback
#         fields = [
#             'name',
#             'city',
#             'email',
#             'mobile',
#             'ticket_support',
#             'it_support',
#             'security',
#             'housekeeping',
#             'facilitators',
#             'archakas',
#             'devotion',
#             'harathi',
#             'fountain',
#             'prasadam',
#             'visit',
#             'improvement_areas',
#         ]

#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
#             'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
#             'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your mobile number'}),
            
#             # Dropdown converted into Radio Select for single-choice
#             'ticket_support': forms.RadioSelect(choices=[
#                 ('Strongly Agree', 'Strongly Agree'),
#                 ('Agree', 'Agree'),
#                 ('Neutral', 'Neutral'),
#                 ('Disagree', 'Disagree'),
#                 ('Strongly Disagree', 'Strongly Disagree'),
#             ]),
#             'it_support': forms.RadioSelect(choices=[
#                 ('Strongly Agree', 'Strongly Agree'),
#                 ('Agree', 'Agree'),
#                 ('Neutral', 'Neutral'),
#                 ('Disagree', 'Disagree'),
#                 ('Strongly Disagree', 'Strongly Disagree'),
#             ]),
#             'security': forms.RadioSelect(choices=[
#                 ('Strongly Agree', 'Strongly Agree'),
#                 ('Agree', 'Agree'),
#                 ('Neutral', 'Neutral'),
#                 ('Disagree', 'Disagree'),
#                 ('Strongly Disagree', 'Strongly Disagree'),
#             ]),
#             'housekeeping': forms.RadioSelect(choices=[
#                 ('Strongly Agree', 'Strongly Agree'),
#                 ('Agree', 'Agree'),
#                 ('Neutral', 'Neutral'),
#                 ('Disagree', 'Disagree'),
#                 ('Strongly Disagree', 'Strongly Disagree'),
#             ]),
#             'facilitators': forms.RadioSelect(choices=[
#                 ('Strongly Agree', 'Strongly Agree'),
#                 ('Agree', 'Agree'),
#                 ('Neutral', 'Neutral'),
#                 ('Disagree', 'Disagree'),
#                 ('Strongly Disagree', 'Strongly Disagree'),
#             ]),
#             'archakas': forms.RadioSelect(choices=[
#                 ('Strongly Agree', 'Strongly Agree'),
#                 ('Agree', 'Agree'),
#                 ('Neutral', 'Neutral'),
#                 ('Disagree', 'Disagree'),
#                 ('Strongly Disagree', 'Strongly Disagree'),
#             ]),
#             'devotion': forms.RadioSelect(choices=[
#                 ('Strongly Agree', 'Strongly Agree'),
#                 ('Agree', 'Agree'),
#                 ('Neutral', 'Neutral'),
#                 ('Disagree', 'Disagree'),
#                 ('Strongly Disagree', 'Strongly Disagree'),
#             ]),
#             'harathi': forms.RadioSelect(choices=[
#                 ('Strongly Agree', 'Strongly Agree'),
#                 ('Agree', 'Agree'),
#                 ('Neutral', 'Neutral'),
#                 ('Disagree', 'Disagree'),
#                 ('Strongly Disagree', 'Strongly Disagree'),
#             ]),
#             'fountain': forms.RadioSelect(choices=[
#                 ('Strongly Agree', 'Strongly Agree'),
#                 ('Agree', 'Agree'),
#                 ('Neutral', 'Neutral'),
#                 ('Disagree', 'Disagree'),
#                 ('Strongly Disagree', 'Strongly Disagree'),
#             ]),
#             'prasadam': forms.RadioSelect(choices=[
#                 ('Strongly Agree', 'Strongly Agree'),
#                 ('Agree', 'Agree'),
#                 ('Neutral', 'Neutral'),
#                 ('Disagree', 'Disagree'),
#                 ('Strongly Disagree', 'Strongly Disagree'),
#             ]),
#             'visit': forms.RadioSelect(choices=[
#                 ('Strongly Agree', 'Strongly Agree'),
#                 ('Agree', 'Agree'),
#                 ('Neutral', 'Neutral'),
#                 ('Disagree', 'Disagree'),
#                 ('Strongly Disagree', 'Strongly Disagree'),
#             ]),
#             'improvement_areas': forms.Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Mention the areas for improvement',
#                 'rows': 4,
#             }),
#         }


from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        name = forms.CharField(max_length=100, required=True)
        city = forms.CharField(max_length=100, required=True)
        email = forms.EmailField(required=True)
        mobile = forms.CharField(max_length=15, required=True)

        # Feedback questions
        CHOICES = [
            ('strongly_agree', 'Strongly Agree'),
            ('agree', 'Agree'),
            ('neutral', 'Neutral'),
            ('disagree', 'Disagree'),
            ('strongly_disagree', 'Strongly Disagree'),
        ]

        ticket_support = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=True)
        it_support = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=True)
        security = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=True)
        housekeeping = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=True)
        facilitators = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=True)
        archakas = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=True)
        devotion = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=True)
        harathi = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=True)
        fountain = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=True)
        prasadam = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=True)
        visit = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=True)

        improvement_areas = forms.CharField(widget=forms.Textarea, required=False)

