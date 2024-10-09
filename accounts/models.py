
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
import uuid


class Country(models.Model):
    name = models.CharField(max_length=25, null=False, blank=False)
    created_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta :
        verbose_name = 'Country'
        verbose_name_plural= 'Countries'
        db_table = 'Countries'


class Profile(AbstractUser):
    email = models.EmailField(_("email address"), blank=False,null=False, unique=True)
    phone_number = models.BigIntegerField(blank=True, null=True, unique=True)
    first_name = models.CharField(_("first name"), max_length=150, blank=False, null=False)
    last_name = models.CharField(_("last name"), max_length=150, blank=False, null=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=False, blank=False)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    created_on = models.DateTimeField(auto_now=True)
    update_on = models.DateTimeField(auto_now=True)

    groups = None
    user_permissions = None

    class Meta:
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

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='devices', null=False, blank=False)
    device_uuid = models.UUIDField(default=uuid.uuid4, editable=False ),
    last_login = models.DateTimeField('last_login', auto_now=True, blank=True, null=True),
    device_type = models.CharField(max_length=25, choices=DEVICE_TYPE_CHOICES, null=False, blank=False ),
    browser = models.CharField(max_length=25, choices=BROWSER_CHOICES, null=True, blank=True )
    device_model = models.CharField(max_length=25, null=True, blank=True )
    ip_address = models.GenericIPAddressField(null=False, blank=False)

    class Meta :
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'
        db_table = 'Devices'
        ordering = ["-user"]




