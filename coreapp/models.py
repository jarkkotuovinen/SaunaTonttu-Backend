from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from coreapp import constants
from coreapp.manager import MyUserManager
from .base import BaseModel


# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='user/', default='user/default.png')
    gender = models.SmallIntegerField(choices=constants.GenderChoices.choices, default=constants.GenderChoices.MALE)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    @cached_property
    def get_image_url(self):
        return f"{settings.MEDIA_HOST}{self.image.url}"


class UserConfirmation(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    confirmation_code = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.confirmation_code} : {self.is_used}"


class LoginHistory(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=100)
    user_agent = models.CharField(max_length=500)
    is_success = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.ip_address} - {self.user_agent} - {self.is_success}"
