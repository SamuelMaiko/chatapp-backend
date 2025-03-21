from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from apis.models import BaseModel

User = get_user_model()


class Chat(BaseModel):
    participant1 = models.ForeignKey(
        User, related_name='chats_participant1', on_delete=models.CASCADE)
    participant2 = models.ForeignKey(
        User, related_name='chats_participant2', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        db_table = 'chats'
        unique_together = ("participant1", "participant2")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(
                f"chat-{self.participant1.username}-{self.participant2.username}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Chat between {self.participant1.username} and {self.participant2.username}"
