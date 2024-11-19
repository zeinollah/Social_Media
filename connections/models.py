from django.db import models
from accounts.models import Profile



class Friendship(models.Model):
    PENDING = "Pending"
    ACCEPTED = "Accepted"
    REJECTED = "Rejected"
    FRIENDSHIP_STATUS_CHOICES = (
        (PENDING, "Pending"),
        (ACCEPTED, "Accepted"),
        (REJECTED, "Rejected"),
    )

    request_sender = models.ForeignKey(Profile, related_name="request_senders", on_delete=models.CASCADE)
    request_receiver = models.ForeignKey(Profile, related_name="request_receivers", on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=FRIENDSHIP_STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = (("request_sender", "request_receiver"),)

