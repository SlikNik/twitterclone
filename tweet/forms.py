from django import forms
from tweet.models import Tweet

class AddTweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ('body',)

