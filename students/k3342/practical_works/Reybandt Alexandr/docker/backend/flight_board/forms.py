from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Employee


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=60, help_text='Имя пользователя')

    class Meta:
        model = Employee
        fields = ['username', 'password1', 'password2']
