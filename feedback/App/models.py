from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    

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
    

    improvement_areas = models.TextField(blank=True, null=True)
    rating = models.TextField(blank=True, null=True)
    quality = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
