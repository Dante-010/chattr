from django.db import models
class ChatRoom(models.Model):
    room_name = models.CharField(max_length=100, primary_key=True)
    creation_date = models.DateTimeField('date created', auto_now=True)

    def __str__(self):
        return self.room_name