from django.contrib import admin
from .models import Room, Message


class RoomAdminConfig(admin.ModelAdmin):
    list_display = ('id', 'creator', 'created_date', 'is_active',)
    list_filter = ('created_date',)
    search_fields = ('sender', 'recipient',)
    

class MessageAdminConfig(admin.ModelAdmin):
    list_display = ('id', 'author', 'image', 'send_date')
    list_filter = ('send_date',)
    search_fields = ('author',)


admin.site.register(Room, RoomAdminConfig)
admin.site.register(Message, MessageAdminConfig)
