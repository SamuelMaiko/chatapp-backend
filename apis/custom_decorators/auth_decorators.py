from functools import wraps
from graphql import GraphQLError


def authentication_required(func):
    @wraps(func)
    def wrapper(self, info, *args, **kwargs):
        if not info.context.user.is_authenticated:
            raise GraphQLError(
                "Authentication required",
                extensions={"code": "UNAUTHORIZED"}
            )
        return func(self, info, *args, **kwargs)
    return wrapper
