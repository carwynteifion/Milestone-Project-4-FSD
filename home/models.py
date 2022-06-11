from django.db import models


class Subscribers(models.Model):
    """
    Model for collecting email addresses
    from newsletter sign-ups
    """
    email = models.CharField(max_length=254)
