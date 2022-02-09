from django.forms import ModelForm
from django import forms
from accounts.models import CATEGORY_CHOICES
from inquire_me.models import Post, Comment


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body", "username",
                  "categories"]


class PostForm(forms.Form):
    title = forms.CharField(max_length=80)
    body = forms.CharField(widget=forms.Textarea)
    created_at = forms.DateTimeField(widget=forms.TextInput(
        attrs={'placeholder': 'YYYY-MM-DD'}))
    categories = forms.ChoiceField(choices=CATEGORY_CHOICES)

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['categories'] = forms.ChoiceField(
            choices=CATEGORY_CHOICES)


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
