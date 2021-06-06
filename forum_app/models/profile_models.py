from django.contrib.auth.forms import UsernameField
from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from django.db.models import TextField, EmailField, CharField, ImageField

class UserProfile(AbstractBaseUser):
    name = CharField(max_length=16, null=False)
    surname = CharField(max_length=16, null=False)
    email = EmailField(null=False, unique=True)
    description = TextField(max_length=128)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']