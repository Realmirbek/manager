# Generated by Django 5.1.6 on 2025-02-10 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0015_alter_candidate_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mentor',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
