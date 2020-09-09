from django.contrib import admin
from tweet.models import Tweet

class TweetAdmin(admin.ModelAdmin):
    list_display = ['tweet_body', 'madeBy', 'date']

admin.site.register(Tweet)
