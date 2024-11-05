from django.contrib import admin
from posts.models import Post, PostFile, Comment


class PostAdmin(admin.ModelAdmin):
    actions = None
    search_fields = ['title', 'author__username']
    list_display = ('id', 'title', 'text', 'author', 'is_public')

admin.site.register(Post, PostAdmin)


class PostFileAdmin(admin.ModelAdmin):
    actions = None
    search_fields = ['post__author__username']
    list_display = ('id', 'post', 'image', 'video', 'file', 'caption')

admin.site.register(PostFile, PostFileAdmin)


class CommentsAdmin(admin.ModelAdmin):
    actions = None
    search_fields = ['comment__author__username']
    list_display = ('id', 'author', 'get_post_title', 'comment', 'created_on')

    def get_post_title(self, obj):
        return obj.post.title
    get_post_title.short_description = 'post'

admin.site.register(Comment, CommentsAdmin)
