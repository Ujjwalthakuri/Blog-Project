from django.contrib.auth.models import User
from .models import *
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def cteate_profile(sender, instance, created, *args, **kwargs):
    if created:
        profileModel.objects.create(User=instance)