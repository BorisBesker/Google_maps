from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class UserForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
