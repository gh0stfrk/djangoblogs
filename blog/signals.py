from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Post, Like


@receiver(post_save, sender=Post)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Like.objects.create(post=instance)
