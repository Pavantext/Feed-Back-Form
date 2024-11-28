from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.feedback_form, name='feedback_form'),
]