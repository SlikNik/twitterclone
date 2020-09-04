from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from twitteruser.forms import SignUpForm


def user_view(request, username):
    current_user = TwitterUser.objects.get(username=username)
    user_tweets = Tweet.objects.filter(madeBy=current_user)
    return render(request, 'user_detail.html', {'current_user': current_user , 'tweets': user_tweets})

@login_required
def follow(request, username):
    follow_user = TwitterUser.objects.get(username=request.user.username)
    add_follower = TwitterUser.objects.get(username=username)
    add_follower.followers.add(follow_user)
    follow_user.following.add(add_follower)
    follow_user.save()
    add_follower.save()
    return HttpResponseRedirect(reverse('homepage'))

def sign_up_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = TwitterUser.objects.create_user(
                username=data.get('username'), 
                password=data.get('password'), 
                email=data.get('email'),
                display_name=data.get('display_name'),
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
            )
            login(request, new_user)
            return HttpResponseRedirect(reverse('homepage'))

    form = SignUpForm()
    return render(request, 'generic_form.html',  {'form': form})

