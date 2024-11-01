from django.contrib import admin
from posts.models import Post, PostFile


class PostAdmin(admin.ModelAdmin):
    actions = None
    search_fields = ['title', 'author__username']
    list_display = ('id', 'title', 'text', 'author', 'is_public')

    def has_add_permission(self, request):
        return False

admin.site.register(Post, PostAdmin)


class PostFileAdmin(admin.ModelAdmin):
    actions = None
    search_fields = ['post__author__username']
    list_display = ('id', 'post', 'image', 'video', 'file', 'caption')

    def has_add_permission(self, request):
        return False

admin.site.register(PostFile, PostFileAdmin)
