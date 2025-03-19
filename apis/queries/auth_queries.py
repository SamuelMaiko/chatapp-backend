import graphene
from apis.types import UserType


class AuthQuery(graphene.ObjectType):
    me = graphene.Field(UserType)

    def resolve_me(self, info):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("Authentication required!")
        return user
