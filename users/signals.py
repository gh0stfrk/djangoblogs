from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import os

from .models import Profile
from django_project.settings import MEDIA_ROOT


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
