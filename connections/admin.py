from django.contrib import admin
from connections.models import Connection

class ConnectionAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('request_sender', 'request_receiver', 'status', 'created_at')
    search_fields = ('request_sender', 'request_receiver')
admin.site.register(Connection, ConnectionAdmin)
