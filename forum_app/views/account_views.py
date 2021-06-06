from forum_app.views.views import registration
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.views.generic import FormView, CreateView, ListView, RedirectView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from forum_app.models.profile_models import Profile

class LogInView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')

class LogOutView(RedirectView):
    pattern_name = 'login.html'
    

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')

class CheckProfileView(ListView):
    model = User
    template_name = 'profile.html'