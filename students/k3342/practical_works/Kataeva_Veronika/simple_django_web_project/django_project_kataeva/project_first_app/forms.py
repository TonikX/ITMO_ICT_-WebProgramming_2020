from django import forms
from project_first_app.models import Car, Owner


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['first_name', 'last_name', 'date_of_birth', 'passport', 'address', 'nationality']

