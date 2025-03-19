import graphene
from apis.custom_decorators import authentication_required
from a_chat.models import Message, Chat
from apis.types import ChatType, MessageType
from django.db.models import Q


class ChatQuery(graphene.ObjectType):
    all_chats = graphene.List(ChatType)
    messages = graphene.List(MessageType)

    def resolve_messages(self, info):
        return Message.objects.all()

    @authentication_required
    def resolve_all_chats(self, info):
        user = info.context.user
        return Chat.objects.filter(Q(participant1=user) | Q(participant2=user))
