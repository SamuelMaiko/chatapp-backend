from django.db import models
from django.contrib.auth import get_user_model
from .Chat import Chat
from apis.models import BaseModel
from django.utils import timezone

User = get_user_model()


class UserChatStatus(BaseModel):
    user = models.ForeignKey(
        User, related_name='chat_statuses', on_delete=models.CASCADE)
    chat = models.ForeignKey(
        Chat, related_name='statuses', on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    last_deleted_at = models.DateTimeField(default=timezone.now)
    last_viewed_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'user_chat_statuses'
        unique_together = ("user", "chat")

    def __str__(self):
        return f"Status of {self.user.first_name} in chat {self.chat.id} with {self.chat.participant1.first_name}-{self.chat.participant2.first_name}"
