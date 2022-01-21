
from django.db import models
from django.contrib.auth.models import AbstractUser


CATEGORY_CHOICES = (
    ('automotive', 'AUTOMOTIVE'),
    ('beauty', 'BEAUTY'),
    ('business', 'BUSINESS'),
    ('engineering', 'ENGINEERING'),
    ('entertainment', 'ENTERTAINMENT'),
    ('financial', 'FINANCIAL'),
    ('health', 'HEALTH'),
    ('history', 'HISTORY'),
    ('language', 'LANGUAGE'),
    ('politics', 'POLITICS'),
    ('programming', 'PROGRAMMING'),
    ('psychology', 'PYSCHOLOGY'),
    ('residential consruction', 'RESIDENTIAL CONSTRUCTION'),
    ('science', 'SCIENCE')
)

COLOR_CHOICES = (
    ('green', 'GREEN'),
    ('blue', 'BLUE'),
    ('red', 'RED'),
    ('grey', 'GREY'),
    ('black', 'BLACK'),
)


class User(AbstractUser):
    username = models.CharField(primary_key=True, max_length=100, null=False)
    birth_date = models.DateField(null=True, blank=True)
    categories_verified = models.CharField(
        max_length=30, choices=CATEGORY_CHOICES, default='')
    color_iqroom = models.CharField(
        max_length=6, choices=COLOR_CHOICES, default='green')

    def __str__(self):
        return self.username


class Color(models.Model):
    color = models.CharField(
        max_length=6, choices=COLOR_CHOICES, default='green')
