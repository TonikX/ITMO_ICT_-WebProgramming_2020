from django import forms
from django.db import models
from django.contrib.auth.models import User
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('email','name','body','datein','dateout','rating')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_check = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password_check',
            'first_name',
            'last_name',
            'email'
        ]
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Ваш никнейм'
        self.fields['password'].label = 'Пароль'
        self.fields['password'].help_text = 'Придумайте пароль'
        self.fields['password_check'].label = 'Повторите пароль'
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['email'].label = 'Почта'
        self.fields['email'].help_text = 'Следует указать действующий адрес'