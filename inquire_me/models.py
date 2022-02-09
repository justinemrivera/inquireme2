from django.db import models
from accounts.models import CATEGORY_CHOICES
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


# User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    categories = models.CharField(
        max_length=30, choices=CATEGORY_CHOICES, default='')
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='post_likes')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post_connected = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.author) + ', ' + self.post_connected.title[:40]


class Category(models.Model):

    CATEGORY_CHOICES = (
        ('Automotive', 'AUTOMOTIVE'),
        ('Beauty', 'BEAUTY'),
        ('Business', 'BUSINESS'),
        ('Engineering', 'ENGINEERING'),
        ('Entertainment', 'ENTERTAINMENT'),
        ('Financial', 'FINANCIAL'),
        ('Health', 'HEALTH'),
        ('History', 'HISTORY'),
        ('Language', 'LANGUAGE'),
        ('Politics', 'POLITICS'),
        ('Programming', 'PROGRAMMING'),
        ('Psychology', 'PYSCHOLOGY'),
        ('Residential Construction', 'RESIDENTIAL CONSTRUCTION'),
        ('Science', 'SCIENCE')
    )
    all_categories = models.CharField(
        choices=CATEGORY_CHOICES, max_length=30, default='')
