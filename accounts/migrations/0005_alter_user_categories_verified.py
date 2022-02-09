# Generated by Django 4.0 on 2022-01-29 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_categories_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='categories_verified',
            field=models.CharField(choices=[('Automotive', 'AUTOMOTIVE'), ('Beauty', 'BEAUTY'), ('Business', 'BUSINESS'), ('Engineering', 'ENGINEERING'), ('Entertainment', 'ENTERTAINMENT'), ('Financial', 'FINANCIAL'), ('Health', 'HEALTH'), ('History', 'HISTORY'), ('Language', 'LANGUAGE'), ('Politics', 'POLITICS'), ('Programming', 'PROGRAMMING'), ('Psychology', 'PYSCHOLOGY'), ('Residential Construction', 'RESIDENTIAL CONSTRUCTION'), ('Science', 'SCIENCE')], default='', max_length=30),
        ),
    ]
