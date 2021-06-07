from forum_app.models.profile_models import Profile
from django.forms import ModelForm

class ProfileForm(ModelForm):
    class Meta:
        model = Profile 
        fields = ['name','surname','email', 'description']