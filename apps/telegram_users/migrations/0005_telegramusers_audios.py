# Generated by Django 5.0.1 on 2024-06-06 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_users', '0004_remove_telegramusers_audios'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramusers',
            name='audios',
            field=models.JSONField(default=dict),
        ),
    ]