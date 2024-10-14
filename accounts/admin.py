from django.contrib import admin

from accounts.models import Profile

admin.site.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')