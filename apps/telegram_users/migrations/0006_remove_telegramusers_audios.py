# Generated by Django 5.0.1 on 2024-06-06 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_users', '0005_telegramusers_audios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telegramusers',
            name='audios',
        ),
    ]
