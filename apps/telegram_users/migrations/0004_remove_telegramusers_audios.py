# Generated by Django 5.0.1 on 2024-06-06 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_users', '0003_alter_telegramusers_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telegramusers',
            name='audios',
        ),
    ]
