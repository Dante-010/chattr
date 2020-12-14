from django.shortcuts import render

from .models import ChatRoom

def index(request):
    return render(request, 'chat/index.html', {
        'chat_rooms': ChatRoom.objects.all()
    })

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })