# Generated by Django 4.0.3 on 2022-06-08 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_result_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
