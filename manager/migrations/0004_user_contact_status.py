# Generated by Django 5.1.6 on 2025-02-08 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_remove_user_contact_status_remove_user_languages_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='contact_status',
            field=models.BooleanField(default=False),
        ),
    ]
