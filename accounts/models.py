from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


import uuid

class CustomUser(AbstractUser):
    username = None
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_("Email Address"), blank=False,unique=True)
    first_name = models.CharField(_('First Name'), blank=False, max_length=100)
    last_name = models.CharField(_('First Name'), blank=False, max_length=100)
    date_of_birth = models.DateField(_("date of birth"), max_length=150, blank=False)
    verified = models.BooleanField(_("verified"), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
    
    
