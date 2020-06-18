from django.db import models
from django import forms

# Create your models here.
class Login(forms.Form):
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)