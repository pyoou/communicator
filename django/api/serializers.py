from rest_framework import serializers
from communicator import models as m


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Room
        fields = ['id', 'creator', 'members', 'created_date', 'is_active']
        

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Message
        fields = ['id', 'room', 'author', 'content', 'image', 'send_date']
