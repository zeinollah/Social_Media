from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, UserManager
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
import uuid




class Account(models.Model):
    email = models.EmailField(_("email address"), blank=True, null=True, unique=True)
    first_name = models.CharField(_("first name"), max_length=150, blank=True, null=True,)
    last_name = models.CharField(_("last name"), max_length=150, blank=True, null=True,)
    username = models.CharField(_("username"), max_length=150, blank=True, null=True,unique=True)
    password = models.CharField(_("password"), max_length=25, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    objects = UserManager()
    class Meta:
        ordering = ("-created_on",)




class Profile(models.Model):
    Gender_Choices = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
    )

    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='profiles')
    phone_number = models.BigIntegerField(blank=True, null=True, unique=True)
    bio = models.TextField(_("bio"), blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6 ,choices=Gender_Choices, blank=True, null=True)
    country = models.CharField(max_length=30, null=False, blank=True, default='country')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        db_table = 'profiles'
        ordering = ["-created_on"]




class Device(models.Model):
    DEVICE_TYPE_CHOICES = (
        ('PC', 'PC'),
        ('IOS', 'IOS'),
        ('Android', 'Android'),
    )
    BROWSER_CHOICES = (
        ('Chrome', 'Chrome'),
        ('Firefox', 'Firefox'),
        ('Safari', 'Safari'),
        ('Opera', 'Opera'),
        ('Other', 'Other'),
    )

    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='devices',)
    device_uuid = models.UUIDField(default=uuid.uuid4, editable=False ),
    last_login = models.DateTimeField(auto_now=True, blank=True, null=True),
    device_type = models.CharField(max_length=25, choices=DEVICE_TYPE_CHOICES, null=True, blank=True ),
    browser = models.CharField(max_length=25, choices=BROWSER_CHOICES, null=True, blank=True )
    device_model = models.CharField(max_length=25, null=True, blank=True )
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    class Meta :
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'
        db_table = 'devices'
        ordering = ["-user"]

