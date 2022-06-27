from django.db import models


class Subscriber(models.Model):
    """
    Model for collecting email addresses
    from newsletter sign-ups
    """
    email = models.EmailField(max_length=254)
    privacy = models.BooleanField()
