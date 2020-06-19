from django import forms
from .models import Register
import re
from django.core.exceptions import ValidationError

class RegisterForms(forms.ModelForm):
    class Meta:
        model = Register
        fields = [
            'first_name',
            'last_name',
            'email',
            'password'
        ]

    def clean_password(self):
        value = self.cleaned_data.get('password')
        password_pattern = "^(?=.*[0-9])(?=.*[A-Z])(?=[a-zA-Z0-9]*[^a-zA-Z0-9][a-zA-Z0-9]*$).{8,}"
        if(re.match(password_pattern, value) == None):
            raise ValidationError("Password doesnt match given format!")
        else:
            return value
    