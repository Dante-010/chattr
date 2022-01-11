from django.contrib import admin
from django import forms

from .models import ChatRoom

class ChatRoomAdminForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = "__all__"

    def clean_room_name(self):
        if ' ' in self.cleaned_data['room_name']:
            raise forms.ValidationError("Can't contain spaces")

        return self.cleaned_data['room_name']

@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    form = ChatRoomAdminForm