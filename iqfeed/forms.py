from django import forms
from .models import Post


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body", "username",
                  "created_at", "catergory_verified", "picture"]
