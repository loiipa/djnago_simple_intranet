from django.shortcuts import redirect, render
import forum_app
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.views.generic import FormView, CreateView, ListView, RedirectView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from forum_app.models.profile_models import Profile
from forum_app.forms.account_forms import ProfileForm
from django.contrib import messages
from django.views.generic.base import View

from django.shortcuts import redirect

# class LogInView(FormView):
# @login_required(redirect_field_name=None)
# class LogInView(LoginView):
#     template_name = 'login.html'
#     form_class = AuthenticationForm
#     redirect_field_name = next
#     pattern_name = reverse_lazy('forum_app:home')
#     login_url = reverse_lazy('forum_app:login')

class LogInView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('forum_app:home')
        form = AuthenticationForm()
        return render(request, 'login.html', {'form' : form })

    def post(self, request):
        if request.user.is_authenticated:
            redirect('forum_app:home')
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('forum_app:home')
        else:
            form = AuthenticationForm()
            return render(request, 'login.html', {'form': form})




class LogOutView(LogoutView):
    def get(self, request):
        logout(request)
        return redirect('forum_app:home')


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('forum_app:home')

    def form_invalid(self, form:UserCreationForm):
        messages.warning(self.request, "Invalid information.")
        return super().form_invalid(form)

class InitProfileView(CreateView):
    form_class = ProfileForm
    template_name = 'profile/register.html'
    context_object_name = 'user_profile'
    success_url = reverse_lazy('forum_app:home')
    login_url = reverse_lazy('forum_app:login')
    def form_invalid(self, form:ProfileForm):
        messages.warning(self.request, "Invalid information.")
        return super().form_invalid(form)

class EditProfileView(UpdateView):
    model = ProfileForm
    template_name = 'profile/register.html'
    context_object_name = 'user_profile'
    fields = ['first_name', 'last_name', 'email', 'description', 'image']
    success_url = reverse_lazy('forum_app:profile_show')
    pk_url_kwargs = 'profile_id'

class ShowProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile/profile.html'
    context_object_name = 'user_profile'
    login_url = reverse_lazy('forum_app:login')
    success_url = reverse_lazy('forum_app:home')
