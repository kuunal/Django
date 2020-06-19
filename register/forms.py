from django import forms
from .models import Register
import re

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
        password_pattern = "^(?=.*[0-9])(?=.*[A-Z])(?=[a-zA-Z0-9]*[^a-zA-Z0-9][a-zA-Z0-9]*$).{8,}"
        password = self.cleaned_data['password']
        print(re.match(password_pattern, password)==None)
        if(re.match(password_pattern, password) == None):
            return forms.ValidationError("Password doesnt match format!")
        else:
            return password
        