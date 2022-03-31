from re import L
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=100)
    name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'password1', 'password2']