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
from forum_app.views.post_views import post
from forum_app.views.post_views import PostView, PostCreateView, PostEditView
from forum_app.views.account_views import LogInView, LogOutView, SignUpView, CheckProfileView

app_name = 'forum_app'

urlpatterns = [
<<<<<<< HEAD
    path('', post_views.PostView.as_view(), name='home'),
    path('login/', account_views.LogInView.as_view(), name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('registration/', views.registration, name='registration'),
    # path('post/<int:post_id>', post_views.ComnentCreateView.as_view(), name='post'),
    path('post/<int:post_id>', post_views.post, name='post'),
    path('post_create/', post_views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:post_id>/edit', post_views.PostEditView.as_view(), name='edit')
=======
    path('', PostView.as_view(), name='home'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('registration/', SignUpView.as_view(), name='registration'),
    path('post/<int:post_id>', post, name='post'),
    path('post_create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:post_id>/edit', PostEditView.as_view(), name='edit')
>>>>>>> bd4f0a9838ef36e3a67adaa276f0339d863e2ae8
]
