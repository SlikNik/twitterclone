from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from twitteruser.forms import SignUpForm

def index(request):
    tweets = Tweet.objects.all()
    return render(request, 'index.html' , {'tweets': tweets})

@login_required
def user_home_view(request):
    tweets = Tweet.objects.all().order_by('-date')
    # following = request.user.followers.all()
    return render(request, 'index.html', {"tweets": tweets})

def user_detail(request, username):
    current_user = TwitterUser.objects.filter(username=username).first()
    tweets = Tweet.objects.filter(
        madeBy=current_user).order_by('-date')
    if current_user.is_authenticated:
        followers = request.user.followers.all()
    else:
        followers = []
    return render(request, 'user_detail.html', {"current_user": current_user, "tweets": tweets, "followers": followers})


def follow_view(request, username):
    current_user = request.user
    following_user = TwitterUser.objects.filter(
        username=username).first()
    current_user.followers.add(following_user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


def unfollow_view(request, username):
    current_user = request.user
    following_user = TwitterUser.objects.filter(
        username=username).first()
    current_user.followers.remove(following_user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

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

