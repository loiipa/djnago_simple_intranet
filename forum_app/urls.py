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
from forum_app.views.post_views import post, post_2
from forum_app.views.post_views import PostView, PostCreateView, PostEditView, PostDeleteView
from forum_app.views.account_views import LogInView, LogOutView, SignUpView, CheckProfileView
# from forum_app.views.post_views import CommentDeleteView
app_name = 'forum_app'

urlpatterns = [
    path('', PostView.as_view(), name='home'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('registration/', SignUpView.as_view(), name='registration'),
    path('post/<int:post_id>/', post, name='post'),
    path('post/<int:post_id>/<int:com_id>/', post_2, name='post_2'),
    # path('post/<int:post_id>/<int:com_id>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('post_create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:post_id>/edit/', PostEditView.as_view(), name='post_edit'),
    path('post/<int:post_id>/delete/', PostDeleteView.as_view(), name='post_delete')
]
