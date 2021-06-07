from django.db.models import TextField
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from forum_app.models.profile_models import Profile
from django import forms

class ProfileForm(forms.ModelForm):
    id = CharField(max_length=64, primary_key=True, unique=True, null=False)
    description = TextField(max_length=128)
    image = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
