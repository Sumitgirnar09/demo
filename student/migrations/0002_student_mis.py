# Generated by Django 4.0.3 on 2022-06-01 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='mis',
            field=models.CharField(default='', max_length=50),
        ),
    ]
