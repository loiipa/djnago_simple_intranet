from django.contrib.auth.forms import UsernameField
from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from django.db.models import TextField, EmailField, CharField, ImageField
from django.db.models.fields import BooleanField
from django.db.models.signals import post_save  
from django.dispatch import receiver

class Profile(models.Model):
    name = models.CharField(max_length=16, null=False)
    surname = models.CharField(max_length=16, null=False)
    email = models.EmailField(null=False)
    description = TextField(max_length=128, blank=True)
    image = ImageField(blank=False)