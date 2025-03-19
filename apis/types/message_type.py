from a_chat.models import Message
import graphene
from graphene_django.types import DjangoObjectType


class MessageType(DjangoObjectType):
    class Meta:
        model = Message
        fields = ("id", "content")
