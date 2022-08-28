# pre_save, post_save, pre_delete, post_delete

from django.db.models.signals import post_save
from django.contrib.auth import get_user_model; User = get_user_model()
from django.dispatch import receiver
from .models import UserProfile


@receiver(signal=post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print(instance)  # the created new user
        user_profile_obj = UserProfile.objects.create(user=instance)  # creating user profile for the instance
        print(user_profile_obj)
