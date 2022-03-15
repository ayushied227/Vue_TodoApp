from django.db import models

# Create your models here.

class Task(models.Model):
    TODO = 'TODO'
    DONE = 'DONE'

    STATUS_CHOICES = (
        (TODO, 'TODO'),
        (DONE, 'DONE'),
    )

    description = models.CharField(max_length=150)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=TODO)