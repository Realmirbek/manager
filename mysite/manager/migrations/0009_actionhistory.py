# Generated by Django 5.1.6 on 2025-02-10 16:25

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0008_remove_candidate_is_deleted_remove_mentor_is_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_type', models.CharField(choices=[('mentor_assigned', 'Ментор назначен'), ('candidate_contacted', 'Стажер связался'), ('candidate_status_changed', 'Статус стажера изменен')], max_length=50)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('details', models.TextField(blank=True, null=True)),
                ('candidate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.candidate')),
                ('mentor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.mentor')),
            ],
        ),
    ]
