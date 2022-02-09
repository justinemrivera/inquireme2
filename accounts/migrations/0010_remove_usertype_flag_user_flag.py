# Generated by Django 4.0 on 2022-02-04 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_remove_user_user_doc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertype',
            name='flag',
        ),
        migrations.AddField(
            model_name='user',
            name='flag',
            field=models.IntegerField(choices=[(1, 'Standard Account'), (2, 'Pro Account')], default=1),
        ),
    ]
