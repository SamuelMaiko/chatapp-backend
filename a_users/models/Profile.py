from django.conf import settings
from django.db import models
from apis.models import BaseModel


class Profile(BaseModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.user.email}'s profile"

    class Meta:
        db_table = 'profiles'
