# teams/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
