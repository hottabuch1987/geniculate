# Generated by Django 3.2.18 on 2023-07-12 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appchat', '0002_auto_20230711_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_online',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Последний визит'),
        ),
    ]