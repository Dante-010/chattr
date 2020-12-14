from django.http import Http404
from django.shortcuts import render

from .models import ChatRoom

def index(request):
    return render(request, 'chat/index.html', {
        'chat_rooms': ChatRoom.objects.all()
    })

def room(request, room_name):
    if ChatRoom.objects.filter(pk=room_name).exists() is False:
        raise Http404("Chat room does not exist.")
    
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })