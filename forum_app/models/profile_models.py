from django.contrib.auth.forms import UsernameField
from django.db import models
from django.contrib.auth.models import User
from django.db.models import TextField, EmailField, CharField, ImageField
from django.db.models.fields import BooleanField

class Profile(models.Model):
    id = models.CharField(max_length=64, primary_key=True, unique=True, null=False)
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    description = TextField(max_length=128, blank=True)
    image = ImageField(blank=False)
