import graphene
from graphene_django import DjangoObjectType
from a_chat.models import Chat
from .user_type import UserType
from .last_message_type import LastMessageType


def get_other_user(self, info):
    user = info.context.user
    return self.participant1 if user == self.participant2 else self.participant2


def chat_last_opened(self, info, who="Me"):
    user = info.context.user
    other_user = get_other_user(self, info)
    return self.statuses.filter(user=other_user if who != "Me" else user).first(
    ).last_viewed_at


class ChatType(DjangoObjectType):
    other_user = graphene.Field(UserType)
    last_message = graphene.Field(LastMessageType)
    unread_messages_count = graphene.Int()

    class Meta:
        model = Chat
        fields = ("id", "slug", "other_user", "last_message")

    def resolve_unread_messages_count(self, info):
        user = info.context.user
        # last time I opened the chat
        last_opened = chat_last_opened(self, info)
        return self.messages.filter(created_at__gt=last_opened).exclude(sender=user).count()

    def resolve_last_message(self, info):
        user = info.context.user
        # is_mine, is_read
        other_user = get_other_user(self, info)
        last_message = self.messages.last()
        if last_message:
            return LastMessageType(
                id=last_message.id,
                content=last_message.content,
                is_mine=last_message.sender == user,
                is_read=chat_last_opened(
                    self, info, who="Other") >= last_message.created_at,
                sent_at=last_message.created_at
                # "sender_id": last_message.sender.id,
            )

        return None

    def resolve_other_user(self, info):
        return get_other_user(self, info)


# NEXT
# - return message is_deleted
# - return chats not deleted by the user
