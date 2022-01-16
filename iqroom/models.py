
from django.db import models


# Create your models here.
COLOR_CHOICES = (
    ('green', 'GREEN'),
    ('blue', 'BLUE'),
    ('red', 'RED'),
    ('grey', 'GREY'),
    ('black', 'BLACK'),
)


class ColorModel(models.Model):
    color = models.CharField(
        max_length=6, choices=COLOR_CHOICES, default='green')
