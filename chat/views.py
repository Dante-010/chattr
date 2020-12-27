from django.http import Http404
from django.shortcuts import render
from django.views import View

from .models import ChatRoom

class IndexView(View):
    template_name = 'chat/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'chat_rooms': ChatRoom.objects.all()
        })

class RoomView(View):
    template_name = 'chat/room.html'

    def get(self, request, room_name, *args, **kwargs):
        if ChatRoom.objects.filter(pk=room_name).exists() == False:
            raise Http404("Chat room does not exist.")

        return render(request, self.template_name, {
            'room_name': room_name
        })