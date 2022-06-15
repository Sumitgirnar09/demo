# Generated by Django 4.0.3 on 2022-06-10 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_student_pass1_student_pass2'),
        ('exam', '0013_remove_question_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='student',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='marks',
            field=models.PositiveIntegerField(default=4),
        ),
    ]
