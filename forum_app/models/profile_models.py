from django.contrib.auth.forms import UsernameField
from django.db import models
from django.contrib.auth.models import User
from django.db.models import TextField, EmailField, CharField, ImageField
from django.db.models.fields import BooleanField

class Profile(models.Model):
    user = models.ForeignKey(User, related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=64, null=True)
    surname = models.CharField(max_length=64, null=True)
    email = models.EmailField(max_length=64, null=True)
    description = models.TextField(max_length=128, blank=True)
    image = models.ImageField(blank=True, null=False)

    def __str__(self):
            return str(self.user)
