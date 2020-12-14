from django.db import models
class ChatRoom(models.Model):
    room_name = models.CharField(max_length=100)
    creation_date = models.DateTimeField('date created')

    def __str__(self):
        return self.room_name