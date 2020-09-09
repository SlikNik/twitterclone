from django.db import models
from twitteruser.models import TwitterUser
from tweet.models import Tweet

class Notification(models.Model):
    receiver = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    track = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    readed = models.BooleanField(default=False)