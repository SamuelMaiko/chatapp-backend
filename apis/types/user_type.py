from django.contrib.auth import get_user_model
import graphene
from graphene_django.types import DjangoObjectType

User = get_user_model()


class UserType(DjangoObjectType):
    profile_picture = graphene.String()

    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", "profile_picture")

    def resolve_profile_picture(self, info):
        # Get the profile picture from the related Profile model
        profile = getattr(self, 'profile', None)
        return profile.profile_picture.url if profile and profile.profile_picture else None
