from django.db import models
from accounts.serializers import User




class Post(models.Model):
    author = models.ForeignKey(User, related_name = "posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=200,blank=False, null=False)
    text = models.TextField(max_length=1000,blank=True,null=True)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']



class PostFile(models.Model):
     post = models.ForeignKey(Post,related_name="post_files", on_delete=models.CASCADE)
     image = models.ImageField(upload_to='image_file/post_image/',blank=True,null=True)
     video = models.FileField(upload_to='image_file/post_video/',blank=True,null=True)
     caption = models.TextField(max_length=500, blank=True, null=True)
     file = models.FileField(upload_to='image_file/post_file/',blank=True,null=True)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     class Meta:
         ordering = ['-created_at']



class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=150, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]
