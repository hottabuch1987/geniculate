# Generated by Django 3.2.18 on 2023-07-12 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appchat', '0003_user_last_online'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_online',
        ),
    ]