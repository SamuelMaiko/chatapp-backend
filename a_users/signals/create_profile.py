from django.db.models.signals import post_save
from django.dispatch import receiver
from a_users.models.CustomUser import CustomUser
from a_users.models.Profile import Profile


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
