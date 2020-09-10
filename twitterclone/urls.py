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
from twitteruser import views as twitteruserviews
from authentication import views as authenticateviews
from tweet import views as tweetviews
from notification import views as notificationviews


urlpatterns = [
    path('', twitteruserviews.Index, name='homepage'),
    path('login/', authenticateviews.login_view, name="loginview"),
    path('logout/', authenticateviews.logout_view, name="logoutview"),
    path('signup/', twitteruserviews.SignUpView, name="signupview"),
    path('profile/<str:username>/', twitteruserviews.user_detail, name='profile'),
    path('tweet/<int:id>/', tweetviews.TweetDetail, name='tweetdetail'),
    path('home/', twitteruserviews.user_home_view, name='userhomepage'),
    path('tweet/', tweetviews.TweetSubmit, name='tweetsubmit'),
    path('notification/', notificationviews.notified, name='notification'),
    path('follow/<str:username>/', twitteruserviews.follow_view, name='follow'),
    path('unfollow/<str:username>/', twitteruserviews.unfollow_view, name='unfollow'),
    path('admin/', admin.site.urls),
]
