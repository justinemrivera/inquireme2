# Generated by Django 4.0.1 on 2022-01-19 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inquire_me', '0005_remove_post_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='username',
        ),
    ]