from django.views.generic import ListView
from forum_app.forms.forms import PostForm
from forum_app.models.models import Post
# from forum_app.models import Post

class PostView(ListView):
	model = Post
	template_name = 'home.html'
	# form_class = PostForm
	# success_url = 'forum_app:home'


