# Generated by Django 4.0.3 on 2022-06-10 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('pass1', models.CharField(default='', max_length=70)),
                ('pass2', models.CharField(default='', max_length=70)),
            ],
        ),
    ]
