from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}), required=True)
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter city name'}), required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter Email address'}), required=True)
    mobile = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Enter mobile number'}), max_length=15, required=True)
    class Meta:
        model = Feedback
        fields = '__all__'
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

        rating = forms.CharField(widget=forms.Textarea, required=False)
        quality = forms.CharField(widget=forms.Textarea, required=False)