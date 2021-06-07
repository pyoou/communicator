from django.shortcuts import render
from communicator import models as m
from .serializers import MessageSerializer, RoomSerializer
from rest_framework import authentication, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response


class RoomAPIView(APIView):
    """
        list of rooms
    """
    # authentication_class = models.Authentication
    # permission_classes = models
    
    def get(self, request, user=None, format=None):
        """
            Return a list of all rooms
        """
        if user is not None:
            room = m.Room.objects.all().filter(members=user)
        else:
            room = m.Room.objects.all()
            
        serializer = RoomSerializer(room, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        """
            Add your elements to list
        """
        serializer = RoomSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        
        
class MessageAPIView(APIView):
    """
        list of messages in room
    """
    # authentication_class = models.Authentication
    # permission_classes = models
    
    def get(self, request, pk, format=None):
        """
            Return a list of messages in room
        """
        message = m.Message.objects.all().filter(room=pk)
        serializer = MessageSerializer(message, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        """
            Add your elements to list
        """
        serializer = MessageSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
                
    