from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class PostReport(models.Model):
    reporter = models.ForeignKey(User,related_name= 'author_reports', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='post_reported', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200 ,blank=True, null=True)
    image = models.ImageField(upload_to='media/post_report_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']



class AccountReport(models.Model):
    reporter = models.ForeignKey(User, related_name= 'reporter_reports', on_delete=models.CASCADE)
    account = models.ForeignKey(User,related_name= 'account_reports', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200 ,blank=True, null=True)
    image = models.ImageField(upload_to='media/account_report_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
