from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _




class Profile(models.Model):
    Gender_Choices = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
    )
    user = models.OneToOneField(User, related_name='profiles', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images_file/account_image', blank=True, null=True)
    phone_number = models.BigIntegerField(blank=True, null=True, unique=True)
    bio = models.TextField(_("bio"),max_length= 150, blank=True, null=True)
    birth_date = models.DateField (blank=True, null=True)
    gender = models.CharField(max_length=6 ,choices=Gender_Choices, blank=True, null=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True) #TODO : user should not see this fild.
    last_login = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f" {self.user.username} Profile"

