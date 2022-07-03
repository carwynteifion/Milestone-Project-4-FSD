from django.contrib import admin
from .models import Subscriber

# Register your models here.


class SubscriberAdmin(admin.ModelAdmin):
    """
    Creates Subscriber model in Admin page
    with email and privacy properties
    """
    list_display = (
        'email',
        'privacy',
    )


admin.site.register(Subscriber, SubscriberAdmin)
