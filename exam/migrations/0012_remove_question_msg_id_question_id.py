# Generated by Django 4.0.3 on 2022-06-10 14:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0011_remove_question_id_question_msg_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='msg_id',
        ),
        migrations.AddField(
            model_name='question',
            name='id',
            field=models.BigAutoField(auto_created=True, default=django.utils.timezone.now, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
