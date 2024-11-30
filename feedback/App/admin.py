from django.contrib import admin
from .models import Feedback
# Register your models here.

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'city', 'mobile', 'ticket_support', 'it_support', 'security', 'housekeeping', 'facilitators', 'archakas', 'devotion', 'harathi', 'fountain', 'prasadam', 'visit', 'improvement_areas', 'rating', 'quality')