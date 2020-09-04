"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitteruser.views import user_view, sign_up_view, follow
from tweet.views import index, tweet_submit
from authentication.views import login_view, logout_view


urlpatterns = [
    path('', index, name='homepage'),
    path('login/', login_view, name="loginview"),
    path('logout/', logout_view, name="logoutview"),
    path('signup/', sign_up_view, name="signupview"),
    path('profile/<str:username>/', user_view, name='profile'),
    path('tweet/', tweet_submit, name='tweetsubmit'),
    path('follow/<str:username>/', follow, name='follow'),
    path('admin/', admin.site.urls),
]
