from django.db import models
from django import forms

# Create your models here.
class ContactForm(forms.Form):
    your_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=200)