from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
import forum_app 
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.views.generic import FormView, CreateView, ListView, RedirectView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from forum_app.models.profile_models import Profile
from forum_app.forms.account_forms import ProfileForm
from django.contrib import messages
from django.views.generic.base import View

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

class InitProfileView(LoginRequiredMixin,CreateView):
    form_class = ProfileForm
    template_name = 'profile/register.html'
    context_object_name = 'user_profile'
    success_url = reverse_lazy('forum_app:home')
    login_url = reverse_lazy('forum_app:login')
    model = Profile
    queryset = model.objects.all().order_by('-id')
    def form_valid(self, form:ProfileForm):
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        return super().form_valid(form)
    def form_invalid(self, form:ProfileForm):
        print(form.errors)
        return super().form_invalid(form)
        
         
 
class EditProfileView(UpdateView, FormView):
    model = ProfileForm
    template_name = 'profile/register.html'
    context_object_name = 'user_profile'
    fields = ['name', 'surname', 'email', 'description', 'image']
    success_url = reverse_lazy('forum_app:profile_show')
    pk_url_kwargs = 'profile_id'


class ShowProfileView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'profile/profile.html'
    context_object_name = 'user_profile'
    login_url = reverse_lazy('forum_app:login')
    success_url = reverse_lazy('forum_app:home')
    def get_queryset(self):
        profile = Profile.objects.filter(user = self.request.user)
        return profile
