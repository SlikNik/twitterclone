from django.db import models
from django.contrib.auth.models import AbstractUser


class TwitterUser(AbstractUser):
    display_name = models.CharField(max_length=120, blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, blank=True)
    REQUIRED_FIELDS = ['display_name', 'first_name', 'last_name', 'email']

    
    def __str__(self):
        return self.username
