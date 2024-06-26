from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Registration(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = '__all__'
