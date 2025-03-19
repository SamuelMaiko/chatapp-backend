import graphene
import graphql_jwt
from apis.types import UserType


class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = graphene.Field(UserType)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)


class AuthMutation(graphene.ObjectType):
    # Login - returns access & refresh tokens
    token_auth = ObtainJSONWebToken.Field()
    # Verifies access token
    verify_token = graphql_jwt.Verify.Field()
    # Get new access token with refresh token
    refresh_token = graphql_jwt.Refresh.Field()
