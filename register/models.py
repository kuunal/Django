import re
from django import forms
from django.db import models

# Create your models here.
class Register(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField( unique= True)
    password = models.CharField(max_length=100)

