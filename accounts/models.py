from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ARTIST = 'ARTIST', 'Artist'
        ADMIN = 'ADMIN', 'Administrator'

    role = models.CharField(max_length=10, choices=Role.choices, default=Role.ARTIST)
    art_style = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)
    contact_number = models.CharField(max_length=20, blank=True)
    profile_photo = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.role = self.Role.ADMIN
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username