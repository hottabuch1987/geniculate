from django.contrib import admin
from .models import Room, Message

from django.contrib import admin



@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = [ 'name','slug']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'room', 'content', 'date_added']
    list_filter = [ 'user','room']



  