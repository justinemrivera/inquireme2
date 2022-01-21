from django.forms import ModelForm
from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length=80)
    body = forms.CharField(max_length=500)
    created_at = forms.DateTimeField(widget=forms.TextInput(
        attrs={'placeholder': 'YYYY-MM-DD'}))
    username = forms.CharField(max_length=30)
    #picture = forms.ImageField()


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
