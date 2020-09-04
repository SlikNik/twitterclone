from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from twitteruser.models import TwitterUser

class TwitterUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Twitter Field Headings',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'display_name',
                    'following',
                    'followers',

                ),
            },
        ),
    )

admin.site.register(TwitterUser, TwitterUserAdmin)