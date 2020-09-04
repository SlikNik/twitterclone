from django.db import models
from django.contrib.auth.models import AbstractUser


class TwitterUser(AbstractUser):
    display_name = models.CharField(max_length=120, blank=True, null=True)
    following = models.ManyToManyField('self', blank=True, related_name='following')
    followers = models.ManyToManyField('self', blank=True, related_name='followers')
    REQUIRED_FIELDS = ['display_name', 'first_name', 'last_name', 'email']

    
    def __str__(self):
        return self.username
