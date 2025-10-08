from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom User model.
    Extends Django's AbstractUser to make email unique and
    easily expandable for future profile fields.
    """
    email = models.EmailField(unique=True)

    # Future custom fields (optional):
    # avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    # bio = models.TextField(blank=True)

    REQUIRED_FIELDS = ['email']  # required for createsuperuser

    def __str__(self):
        return self.username
