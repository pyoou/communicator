from django.urls import path
from . import views as v


urlpatterns = [
    path('room/', v.RoomAPIView.as_view(), name='RoomApiView'),
    path('room/<int:user>/', v.RoomAPIView.as_view(), name='RoomApiView'),
    path('message/<int:pk>/', v.MessageAPIView.as_view(), name='MessageApiView'),
]
