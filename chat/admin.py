from django.contrib import admin

from .models import ChatRoom

class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ("room_name", "creation_date")

admin.site.register(ChatRoom, ChatRoomAdmin)