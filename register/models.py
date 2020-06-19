import re
from django import forms
from django.db import models

# Create your models here.
class Register(models.Model):
    first_name = models.CharField(max_length=100,)
    last_name = models.CharField(max_length=100,)
    email = models.EmailField(max_length=100, unique= True,)
    password = models.CharField(max_length=100,)

    def clean_email(self):
        email_pattern = "^[a-zA-Z0-9]+[\\.\\-\\+\\_]?[a-zA-Z0-9]+@[a-zA-Z0-9]+[.]?[a-zA-Z]{2,4}[\\.]?([a-z]{2,4})?$"
        email = self.cleaned_data['email']
        if(re.match(email_pattern,email)):
            return email
        else:
            return forms.ValidationError("This is not a valid email")

    def clean_password(self):
        password_pattern = "^(?=.*[0-9])(?=.*[A-Z])(?=[a-zA-Z0-9]*[^a-zA-Z0-9][a-zA-Z0-9]*$).{8,}"
        password = self.cleaned_data['password']
        if(re.match(password_pattern, password)):
            return password
        return forms.ValidationError("Password doesnt match format!")
        