from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.views.generic import FormView, CreateView, ListView, RedirectView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from forum_app.models.profile_models import Profile
from forum_app.forms.account_forms import ProfileForm
from django.contrib import messages

# class LogInView(FormView):
class LogInView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')


class LogOutView(LogoutView):
    permanent = False
    quary_string = True
    success_url =  reverse_lazy('home')
        

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('home')
    def form_invalid(self, form:UserCreationForm):
        messages.warning(self.request, "Invalid information.")
        return super().form_invalid(form)
        

class CheckProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile.html'
    slug_field = "username"
    context_object_name = 'user_profile'
