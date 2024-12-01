from django.contrib import admin
from reports.models import PostReport, AccountReport


class PostReportAdmin(admin.ModelAdmin):
    actions = None
    list_display = [
        'id',
        'reporter',
        'title',
        'description',
        'image',
        'post_reported',
        'author_post',
        'post_title',
    ]
    list_filter = ['reporter', 'post']
    list_display_links = ('id', 'title')
    date_hierarchy = 'created_at'


    def author_post(self,attrs):
        return attrs.post.author.username if attrs.post.author else None
    author_post.short_description = 'Post Reported Auther '

    def post_reported(self,attrs):
        return attrs.post.id  if not attrs.post else None
    post_reported.short_description = 'Post Reported '

    def post_title(self,attrs):
        return attrs.post.title if not attrs.post else None
    post_title.short_description = 'Post Title'

admin.site.register(PostReport, PostReportAdmin)


class AccountReportAdmin(admin.ModelAdmin):
    actions = None
    list_display = ['id', 'reporter', 'title', 'description', 'image', 'account']
    list_filter = ['reporter', 'account']
    list_display_links = ('id', 'title')
    date_hierarchy = 'created_at'

admin.site.register(AccountReport, AccountReportAdmin)


