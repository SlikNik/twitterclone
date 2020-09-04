from django.db import models
from django.utils import timezone
from twitteruser.models import TwitterUser


class Tweet(models.Model):
    body = models.CharField(max_length=140)
    madeBy = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.madeBy.username
    
    @property
    def age(self):
        return int((timezone.now() - self.date).days / 365.25)