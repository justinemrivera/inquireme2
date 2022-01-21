from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import CATEGORY_CHOICES
from .models import User, Color
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomUserCreationForm(UserCreationForm.Meta):
    model = User
    fields = UserCreationForm.Meta.fields + \
        ('username', 'first_name', 'last_name', 'password', 'birth_date',
         'categories_verified', 'color_iqroom')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = UserChangeForm.Meta.fields


class MyModelForm(ModelForm):
    class Meta:
        model = Color
        fields = ['color']


# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=50)
#     password = forms.CharField(max_length=50)


# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)


class SignUpProForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    birth_date = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'YYYY-MM-DD'}))
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    category_verified = forms.ChoiceField(choices=CATEGORY_CHOICES)
