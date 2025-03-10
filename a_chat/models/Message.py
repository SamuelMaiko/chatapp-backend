from django.db import models
from django.contrib.auth import get_user_model
from .Chat import Chat
from apis.models import BaseModel

User = get_user_model()


class Message(BaseModel):
    content = models.TextField()
    sender = models.ForeignKey(
        User, related_name='messages', on_delete=models.CASCADE)
    chat = models.ForeignKey(
        Chat, related_name='messages', on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'messages'

    def __str__(self):
        return f"Message from {self.sender.username} in chat {self.chat.id}"
