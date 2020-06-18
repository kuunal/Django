from django import forms
from .models import Register

class RegisterForms(forms.ModelForm):
    class Meta:
        model = Register
        fields = [
            'first_name',
            'last_name',
            'email',
            'password'
        ]