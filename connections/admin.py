from django.contrib import admin

from connections.models import Friendship


class FriendshipAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('request_sender', 'request_receiver', 'status', 'created_at')
    search_fields = ('request_sender', 'request_receiver')
admin.site.register(Friendship, FriendshipAdmin)
