# from django.db import models

# class Feedback(models.Model):
#     name = models.CharField(max_length=100)
#     city = models.CharField(max_length=100, null=True)
#     email = models.EmailField()
#     mobile = models.CharField(max_length=15)

  
    # ticket_support_strongly_agree = models.BooleanField(default=False)
    # ticket_support_agree = models.BooleanField(default=False)
    # ticket_support_neutral = models.BooleanField(default=False)
    # ticket_support_disagree = models.BooleanField(default=False)
    # ticket_support_strongly_disagree = models.BooleanField(default=False)

    # it_support_strongly_agree = models.BooleanField(default=False)
    # it_support_agree = models.BooleanField(default=False)
    # it_support_neutral = models.BooleanField(default=False)
    # it_support_disagree = models.BooleanField(default=False)
    # it_support_strongly_disagree = models.BooleanField(default=False)

    # security_team_strongly_agree = models.BooleanField(default=False)
    # security_team_agree = models.BooleanField(default=False)
    # security_team_neutral = models.BooleanField(default=False)
    # security_team_disagree = models.BooleanField(default=False)
    # security_team_strongly_disagree = models.BooleanField(default=False)

    # house_keeping_strongly_agree = models.BooleanField(default=False)
    # house_keeping_agree = models.BooleanField(default=False)
    # house_keeping_neutral = models.BooleanField(default=False)
    # house_keeping_disagree = models.BooleanField(default=False)
    # house_keeping_strongly_disagree = models.BooleanField(default=False)

    # facilitator_strongly_agree = models.BooleanField(default=False)
    # facilitator_agree = models.BooleanField(default=False)
    # facilitator_neutral = models.BooleanField(default=False)
    # facilitator_disagree = models.BooleanField(default=False)
    # facilitator_strongly_disagree = models.BooleanField(default=False)

    # archakas_strongly_agree = models.BooleanField(default=False)
    # archakas_agree = models.BooleanField(default=False)
    # archakas_neutral = models.BooleanField(default=False)
    # archakas_disagree = models.BooleanField(default=False)
    # archakas_strongly_disagree = models.BooleanField(default=False)

    # devotion_strongly_agree = models.BooleanField(default=False)
    # devotion_agree = models.BooleanField(default=False)
    # devotion_neutral = models.BooleanField(default=False)
    # devotion_disagree = models.BooleanField(default=False)
    # devotion_strongly_disagree = models.BooleanField(default=False)

    # harathi_strongly_agree = models.BooleanField(default=False)
    # harathi_agree = models.BooleanField(default=False)
    # harathi_neutral = models.BooleanField(default=False)
    # harathi_disagree = models.BooleanField(default=False)
    # harathi_strongly_disagree = models.BooleanField(default=False)

    # fountain_strongly_agree = models.BooleanField(default=False)
    # fountain_agree = models.BooleanField(default=False)
    # fountain_neutral = models.BooleanField(default=False)
    # fountain_disagree = models.BooleanField(default=False)
    # fountain_strongly_disagree = models.BooleanField(default=False)

    # prasadam_strongly_agree = models.BooleanField(default=False)
    # prasadam_agree = models.BooleanField(default=False)
    # prasadam_neutral = models.BooleanField(default=False)
    # prasadam_disagree = models.BooleanField(default=False)
    # prasadam_strongly_disagree = models.BooleanField(default=False)

    # visit_strongly_agree = models.BooleanField(default=False)
    # visit_agree = models.BooleanField(default=False)
    # visit_neutral = models.BooleanField(default=False)
    # visit_disagree = models.BooleanField(default=False)
    # visit_strongly_disagree = models.BooleanField(default=False)

    # improvement_area = models.TextField(blank=True, null=True)

    # def __str__(self):
    #     return self.name

    # FEEDBACK_CHOICES = [
    #     ('strongly_agree', 'Strongly Agree'),
    #     ('agree', 'Agree'),
    #     ('neutral', 'Neutral'),
    #     ('disagree', 'Disagree'),
    #     ('strongly_disagree', 'Strongly Disagree'),
    # ]

    # ticket_support = models.CharField(max_length=20, choices=FEEDBACK_CHOICES)   
    # it_support = models.CharField(max_length=20, choices=FEEDBACK_CHOICES)
    # security = models.CharField(max_length=20, choices=FEEDBACK_CHOICES)
    # housekeeping = models.CharField(max_length=20, choices=FEEDBACK_CHOICES)
    # facilitators = models.CharField(max_length=20, choices=FEEDBACK_CHOICES)
    # archakas = models.CharField(max_length=20, choices=FEEDBACK_CHOICES)
    # devotion = models.CharField(max_length=20, choices=FEEDBACK_CHOICES)
    # harathi = models.CharField(max_length=20, choices=FEEDBACK_CHOICES)
    # fountain = models.CharField(max_length=20, choices=FEEDBACK_CHOICES)
    # prasadam = models.CharField(max_length=20, choices=FEEDBACK_CHOICES)
    # visit = models.CharField(max_length=20, choices=FEEDBACK_CHOICES)
    
    # improvement_area = models.TextField(blank=True, null=True)

    # def __str__(self):
    #     return self.name

from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    
    # Radio select fields
    ticket_support = models.CharField(max_length=20)
    it_support = models.CharField(max_length=20)
    security = models.CharField(max_length=20)
    housekeeping = models.CharField(max_length=20)
    facilitators = models.CharField(max_length=20)
    archakas = models.CharField(max_length=20)
    devotion = models.CharField(max_length=20)
    harathi = models.CharField(max_length=20)
    fountain = models.CharField(max_length=20)
    prasadam = models.CharField(max_length=20)
    visit = models.CharField(max_length=20)
    
    # Text area
    improvement_areas = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
