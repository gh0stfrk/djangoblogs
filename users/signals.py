from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

import os

from .models import Profile
from django_project.settings import MEDIA_ROOT


def create_user_directory(username):
    try:
        os.makedirs(os.path.join(MEDIA_ROOT, "users", username))
    except Exception as e:
        print(e)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        username = instance.get_username()
        create_user_directory(username)
        Profile.objects.create(user=instance)
