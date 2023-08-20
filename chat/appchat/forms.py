from django.contrib.auth.forms import UserCreationForm
from appchat.models import User
from captcha.fields import CaptchaField
from .models import FeedBack

from django import forms


class SignUpForm(UserCreationForm):
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'captcha']


class FeedBackForm(forms.Form):
    email = forms.EmailField(label='E-mail', required=True)
    name = forms.CharField(max_length=55, label='Имя', required=True)
    message = forms.CharField(max_length=255, label='Сообщение', required=True)


class EditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'email', 'location', 'bio', 'avatar')




