from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('chat/<str:room_name>/', views.RoomView.as_view(), name='room'),
]