# Generated by Django 4.0.3 on 2022-06-07 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='testName',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
