from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models.models import Post, Comment


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
