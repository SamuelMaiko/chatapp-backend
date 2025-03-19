import graphene
from apis.queries import ChatQuery, AuthQuery
from apis.mutations import AuthMutation


class Query(ChatQuery, AuthQuery, graphene.ObjectType):
    pass


class Mutation(AuthMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
