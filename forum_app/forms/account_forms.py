from django.db.models import TextField
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.db.models import ImageField
from django.forms.models import ModelForm
from forum_app.models.profile_models import Profile
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','surname','email', 'description', 'image']
