from multiprocessing.resource_tracker import register

from django.contrib import admin

from chats.models import Chat


class ChatAdmin(admin.ModelAdmin):
    actions = None
    list_display = (
        'id',
        'sender',
        'receiver',
        'content',
        'image',
        'video',
        'audio',
        'file',
        'created_at',
    )
    list_display_links = ('id',)
    search_fields = ('sender', 'receiver')

admin.site.register(Chat, ChatAdmin)
