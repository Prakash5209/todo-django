from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from useraccount.managers import CustomUserManager

class CustomUserModel(AbstractUser):
    username=None
    email=models.EmailField(_('email address'),unique=True)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    
    objects=CustomUserManager()
    
    def __str__(self):
        return self.email