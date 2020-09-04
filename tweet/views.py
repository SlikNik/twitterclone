from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from tweet.forms import AddTweetForm


def index(request):
    tweets = Tweet.objects.all()
    return render(request, 'index.html' , {'tweets': tweets})

@login_required
def tweet_submit(request):
    if request.method == 'POST':
        form = AddTweetForm(request.POST)
        if form.is_valid():
            new_tweet = form.save(commit=False)
            new_tweet.madeBy = TwitterUser.objects.filter(username=request.user.username).first()
            new_tweet.save()
            return HttpResponseRedirect(reverse('homepage'))
    form = AddTweetForm()
    return render(request, 'generic_form.html', {'form': form})