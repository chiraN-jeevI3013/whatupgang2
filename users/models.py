from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_admin_user = models.BooleanField(default=True)  # True for now (admin-only MVP)
