from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import TwitterUser, Tweet, Notification

@login_required
def notified(request):
    notifications = Notification.objects.filter(receiver=request.user)
    count = 0
    new_notifications = []
    for notification in notifications:
        if notification.readed == False:
            new_notifications.append(notification.track)
            notification.readed = True
            count += 1
            notification.save()
    return render(request, 'notification.html', {"new": new_notifications, "count": count})