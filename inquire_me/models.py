from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    #picture = models.ImageField(null=True)

    def __str__(self):
        return self.title
