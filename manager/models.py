from django.db import models
from django.utils import timezone

class Mentor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=20, default=0)


    def __str__(self):
        return self.name

class Candidate(models.Model):
    DIRECTION_CHOICES = [
        ('Backend', 'Backend'),
        ('Frontend', 'Frontend'),
        ('Backend (Java)', 'Backend (Java)'),
        ('Backend (Python)', 'Backend (Python)'),
    ]

    STATUS_CHOICES = [
        ('thinking', 'Думает'),
        ('contacted', 'Связались'),

    ]

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, default='default@gmail.com')
    phone = models.CharField(max_length=20, default=0)
    direction = models.CharField(max_length=50, choices=DIRECTION_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='thinking')
    mentor = models.ForeignKey(Mentor, on_delete=models.SET_NULL, null=True, blank=True)



    def __str__(self):
        return self.name


class ActionHistory(models.Model):
    ACTION_CHOICES = [
        ('mentor_assigned', 'Ментор назначен'),
        ('candidate_contacted', 'Стажер связался'),
        ('candidate_status_changed', 'Статус стажера изменен'),
        # Можно добавить другие действия
    ]

    action_type = models.CharField(max_length=50, choices=ACTION_CHOICES)
    candidate = models.ForeignKey('Candidate', on_delete=models.CASCADE, null=True, blank=True)
    mentor = models.ForeignKey('Mentor', on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)  # Время события
    details = models.TextField(blank=True, null=True)  # Дополнительные детали, например, комментарии

    def __str__(self):
        return f"{self.get_action_type_display()} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"




