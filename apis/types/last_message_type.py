import graphene


class LastMessageType(graphene.ObjectType):
    id = graphene.Int()
    content = graphene.String()
    is_mine = graphene.Boolean()
    is_read = graphene.Boolean()
    sent_at = graphene.DateTime()
