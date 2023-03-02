from django.db import models
from enum import Enum

class Priority(Enum):
    Most = 0
    More = 1
    Moderate = 2
    Less = 3
    Least = 4
    Null = 5

class Todo(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField('Created', auto_now_add=True)
    update_at = models.DateTimeField('Updated', auto_now=True)
    isCompleted = models.BooleanField(default=False)
    priority = models.IntegerField(choices=[(item.value, item.name) for item in Priority], default=Priority.Null.value)

    @property
    def priority_name(self):
        return Priority(self.priority).name

    def __str__(self):
        return self.title
