from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField
from .models import User


class SignUpForm(UserCreationForm):
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1',
                  'password2', 'captcha')


class LoginForm(AuthenticationForm):
    captcha = CaptchaField()
    