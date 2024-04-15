from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from user_panel.models import Profile, CustomUser


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(pre_delete, sender=CustomUser)
def delete_profile(sender, instance, **kwargs):
    Profile.objects.get(user=instance).delete()

