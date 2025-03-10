from django.dispatch import receiver
from django.db.models.signals import post_save
from a_chat.models import Chat, UserChatStatus


@receiver(post_save, sender=Chat)
def create_chat_status(sender, instance, **kwargs):
    # checking if the chat is a self chat
    if instance.participant1 == instance.participant2:
        UserChatStatus.objects.create(
            user=instance.participant1, chat=instance)

    # if is a chat between two users
    else:
        UserChatStatus.objects.create(
            user=instance.participant1, chat=instance)
        UserChatStatus.objects.create(
            user=instance.participant2, chat=instance)
