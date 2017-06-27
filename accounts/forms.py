from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


User = get_user_model()


class UserForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) > 20:
            raise ValidationError("User name cannot be more than 20 characters long")
        return password

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) > 20:
            raise ValidationError("User name cannot be more than 20 characters long")
        return username


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
