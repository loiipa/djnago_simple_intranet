"""rush01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.auth.decorators import login_required
from forum_app.views.post_views import PostView
from forum_app.views.account_views import LogInView, LogOutView, SignUpView, CheckProfileView

app_name = 'forum_app'

urlpatterns = [
    path('', PostView.as_view(), name='home'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', login_required(LogOutView.as_view()), name='logout'),
    path('registration/', SignUpView.as_view(), name='registration'),
    # path('post/<int:post_id>', views.post, name='post'),
    path('profile/<slug:user_id>/', CheckProfileView.as_view(), name='profile'),
]
