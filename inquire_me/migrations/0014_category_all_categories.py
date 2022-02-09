# Generated by Django 4.0 on 2022-02-03 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquire_me', '0013_remove_category_all_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='all_categories',
            field=models.CharField(choices=[('Automotive', 'AUTOMOTIVE'), ('Beauty', 'BEAUTY'), ('Business', 'BUSINESS'), ('Engineering', 'ENGINEERING'), ('Entertainment', 'ENTERTAINMENT'), ('Financial', 'FINANCIAL'), ('Health', 'HEALTH'), ('History', 'HISTORY'), ('Language', 'LANGUAGE'), ('Politics', 'POLITICS'), ('Programming', 'PROGRAMMING'), ('Psychology', 'PYSCHOLOGY'), ('Residential Construction', 'RESIDENTIAL CONSTRUCTION'), ('Science', 'SCIENCE')], default='', max_length=30),
        ),
    ]