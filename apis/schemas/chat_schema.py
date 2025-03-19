import graphene
from apis.types import ChatType
from apis.models import Chat
from apis.custom_decorators import authentication_required


class ChatQuery(graphene.ObjectType):
    all_chats = graphene.List(ChatType)

    @authentication_required
    def resolve_all_chats(self, info):
        return Chat.objects.all()
