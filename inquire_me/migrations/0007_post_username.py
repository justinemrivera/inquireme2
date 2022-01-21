# Generated by Django 4.0.1 on 2022-01-19 04:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inquire_me', '0006_remove_post_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='username',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
