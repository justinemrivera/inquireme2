
from django import forms
from django.forms import ModelForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import User, Color, CATEGORY_CHOICES, UserType


class CustomUserCreationForm(UserCreationForm.Meta):
    model = User
    fields = UserCreationForm.Meta.fields + \
        ('username', 'first_name', 'last_name', 'password', 'birth_date',
         'categories_verified', 'color_iqroom', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = UserChangeForm.Meta.fields


class MyModelForm(ModelForm):
    class Meta:
        model = Color
        fields = ['color']


class SignUpProForm(forms.Form):

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    birth_date = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'YYYY-MM-DD'}))
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(max_length=50)
    category_verified = forms.ChoiceField(choices=CATEGORY_CHOICES)


# users/forms.py


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name",
                  "birth_date", "categories_verified", "flag")
        flag = forms.ChoiceField(
            choices=((1, 'Standard'), (2, 'Pro')), initial=1)
        category_verified = forms.ChoiceField(choices=CATEGORY_CHOICES)

    widgets = {

        'username': forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}),
        'email': forms.TextInput(attrs={'class': 'form-control'}),
        'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        'birth_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'YYYY/MM/DD'}),
        'flag': forms.Select(attrs={'class': 'form-control'}),
        'category_verified': forms.Select(attrs={'class': 'form-control'}),
        'password1': forms.TextInput(attrs={'class': 'form-control'}),
        'password2': forms.TextInput(attrs={'class': 'form-control'})
        # 'user_doc': forms.FileInput(attrs={'class': 'form-control-file',}),
    }


class LogInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
