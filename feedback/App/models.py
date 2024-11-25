from django.db import models

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True)
    mobile = models.CharField(max_length=12)
    
    
    ticket_support = models.CharField(max_length=20, choices=[('Strongly Agree', 'Strongly Agree'), ('Agree', 'Agree'), ('Neutral', 'Neutral'), ('Disagree', 'Disagree'), ('Strongly Disagree', 'Strongly Disagree')])
    it_support = models.CharField(max_length=20, choices=[('Strongly Agree', 'Strongly Agree'), ('Agree', 'Agree'), ('Neutral', 'Neutral'), ('Disagree', 'Disagree'), ('Strongly Disagree', 'Strongly Disagree')])
    security_support = models.CharField(max_length=20, choices=[('Strongly Agree', 'Strongly Agree'), ('Agree', 'Agree'), ('Neutral', 'Neutral'), ('Disagree', 'Disagree'), ('Strongly Disagree', 'Strongly Disagree')])
    housekeeping = models.CharField(max_length=20, choices=[('Strongly Agree', 'Strongly Agree'), ('Agree', 'Agree'), ('Neutral', 'Neutral'), ('Disagree', 'Disagree'), ('Strongly Disagree', 'Strongly Disagree')])
    facilitators = models.CharField(max_length=20, choices=[('Strongly Agree', 'Strongly Agree'), ('Agree', 'Agree'), ('Neutral', 'Neutral'), ('Disagree', 'Disagree'), ('Strongly Disagree', 'Strongly Disagree')])
    archakas_guidance = models.CharField(max_length=20, choices=[('Strongly Agree', 'Strongly Agree'), ('Agree', 'Agree'), ('Neutral', 'Neutral'), ('Disagree', 'Disagree'), ('Strongly Disagree', 'Strongly Disagree')])
    devotion_experience = models.CharField(max_length=20, choices=[('Strongly Agree', 'Strongly Agree'), ('Agree', 'Agree'), ('Neutral', 'Neutral'), ('Disagree', 'Disagree'), ('Strongly Disagree', 'Strongly Disagree')])
    harathi_experience = models.CharField(max_length=20, choices=[('Strongly Agree', 'Strongly Agree'), ('Agree', 'Agree'), ('Neutral', 'Neutral'), ('Disagree', 'Disagree'), ('Strongly Disagree', 'Strongly Disagree')])
    fountain_laser_show = models.CharField(max_length=20, choices=[('Strongly Agree', 'Strongly Agree'), ('Agree', 'Agree'), ('Neutral', 'Neutral'), ('Disagree', 'Disagree'), ('Strongly Disagree', 'Strongly Disagree')])
    prasadam_feedback = models.CharField(max_length=20, choices=[('Strongly Agree', 'Strongly Agree'), ('Agree', 'Agree'), ('Neutral', 'Neutral'), ('Disagree', 'Disagree'), ('Strongly Disagree', 'Strongly Disagree')])
    revisit_feedback = models.CharField(max_length=20, choices=[('Strongly Agree', 'Strongly Agree'), ('Agree', 'Agree'), ('Neutral', 'Neutral'), ('Disagree', 'Disagree'), ('Strongly Disagree', 'Strongly Disagree')])
    

    improvement_area = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name