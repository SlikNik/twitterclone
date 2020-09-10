from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from tweet.forms import AddTweetForm
from twitteruser.models import TwitterUser
from notification.models import Notification
from tweet.models import Tweet
import re



# @login_required
# def tweet_submit(request):
#     if request.method == "POST":
#         form = AddTweetForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             new_tweet = Tweet.objects.create(
#                 body=data.get('body'),
#                 madeBy=request.user
#             )
#             mentions = re.findall(r'@(\w+)', data.get('body'))
#             if mentions:
#                 for mention in mentions:
#                     match = TwitterUser.objects.get(username=mention)
#                     if match:
#                         Notification.objects.create(
#                             receiver=match, track=new_tweet)
#             return HttpResponseRedirect(reverse("userhomepage"))
#     form = AddTweetForm()
#     return render(request, 'generic_form.html', {'form': form})

class TweetSubmit(LoginRequiredMixin, TemplateView):

    def get(self, request):
        form = AddTweetForm()
        return render(request, 'generic_form.html', {'form': form})
    
    def post(self, request):
        form = AddTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_tweet = Tweet.objects.create(
                body=data.get('body'),
                madeBy=request.user
            )
            mentions = re.findall(r'@(\w+)', data.get('body'))
            if mentions:
                for mention in mentions:
                    match = TwitterUser.objects.get(username=mention)
                    if match:
                        Notification.objects.create(
                            receiver=match, track=new_tweet)
            return HttpResponseRedirect(reverse("userhomepage"))
        else:
            return render(request, 'generic_form.html', {'form': form})

# def tweet_detail(request, id):
#     tweet_detail = Tweet.objects.get(id=id)
#     return render(request, 'tweet_detail.html', {"tweet": tweet_detail})

class TweetDetail(TemplateView):

    def get(self, request, id):
        tweet_detail = Tweet.objects.get(id=id)
        return render(request, 'tweet_detail.html', {"tweet": tweet_detail})