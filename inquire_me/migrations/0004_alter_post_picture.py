# Generated by Django 4.0.1 on 2022-01-19 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquire_me', '0003_alter_post_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]