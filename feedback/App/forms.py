from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        widgets = {
        'improvement_area': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }
