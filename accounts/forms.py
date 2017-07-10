from django import forms
from django.contrib.auth import authenticate,login


class UserForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        if not user:
            raise forms.ValidationError('Invalid credentials')
        elif not user.is_active:
            raise forms.ValidationError('Disabled account')

        return super(UserForm, self).clean(*args, **kwargs)
