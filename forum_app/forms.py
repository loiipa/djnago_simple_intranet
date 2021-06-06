from django.db import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment

class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']

class PostForm(ModelForm):
	class Meta:
		model = Post
		# fields = ['title', 'author', 'content', 'created']
		fields = ['title', 'content']

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		# fields = ['post', 'author', 'content', 'created']
		fields = ['content']
