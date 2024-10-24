from django.contrib import admin

from accounts.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    actions = None

    list_display = ('get_username', 'get_full_name', 'get_email')

    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'user__email']

    def get_username(self, obj):
        return obj.user.username

    get_username.short_description = 'Username'

    def get_full_name(self, obj):
        first_name = obj.user.first_name.capitalize() if obj.user.first_name else ''
        last_name = obj.user.last_name.capitalize() if obj.user.last_name else ''
        return f"{first_name} {last_name}".strip()

    get_full_name.short_description = 'Full Name'

    def get_email(self, obj):
        return obj.user.email

    get_email.short_description = 'Email'

admin.site.register(Profile, ProfileAdmin)