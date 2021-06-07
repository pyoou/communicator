from django.db import models
from core import settings
from django.utils.translation import gettext_lazy as _


class Room(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, to_field='id')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="members")
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.id)
    
    
class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.RESTRICT, to_field='id', related_name='message_conversation')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, 
                               on_delete=models.RESTRICT, to_field='id')
    content = models.CharField(_('message content'), max_length=255)
    image = models.ImageField(_('image'), upload_to='images/', blank=True, null=True)
    send_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)
