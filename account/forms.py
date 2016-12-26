from django import forms
from account.models import ExtendedUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationFormWithMail(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserCreationFormWithMail, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class AutoUserForm(forms.ModelForm):

    class Meta:
        model = ExtendedUser
        fields = ['presentation']

class LoginForm(forms.ModelForm):
    fields = ['username_for_log', 'password_for_log']
