from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        widgets = {
            'ticket_support': forms.RadioSelect,
            'it_support': forms.RadioSelect,
            'security_support': forms.RadioSelect,
            'housekeeping': forms.RadioSelect,
            'facilitators': forms.RadioSelect,
            'archakas_guidance': forms.RadioSelect,
            'devotion_experience': forms.RadioSelect,
            'harathi_experience': forms.RadioSelect,
            'fountain_laser_show': forms.RadioSelect,
            'prasadam_feedback': forms.RadioSelect,
            'revisit_feedback': forms.RadioSelect,

            'improvement_area': forms.Textarea(attrs={'rows': 3}),
        }
