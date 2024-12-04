from django.db import models
from accounts.serializers import User




class Chat(models.Model):
    sender = models.ForeignKey(User, related_name='massage_sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='massage_receiver', on_delete=models.CASCADE)
    content = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='media/massages/image', blank=True, null=True)
    video = models.FileField(upload_to='media/massages/video', blank=True, null=True)
    audio = models.FileField(upload_to='media/massages/audio', blank=True, null=True)
    file = models.FileField(upload_to='media/massages/file', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']