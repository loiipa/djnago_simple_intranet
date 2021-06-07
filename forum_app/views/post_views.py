from django.views.generic import ListView, CreateView, UpdateView
from forum_app.forms import PostForm, CommentForm
from forum_app.models.models import Post, Comment
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, reverse
from django.core.paginator import Paginator

from django.shortcuts import get_object_or_404

# from forum_app.models import Post

class PostView(ListView):
	model = Post
	template_name = 'home.html'
	paginate_by = 10
	context_object_name = 'post_list'

	def get_queryset(self):
		post_list = Post.objects.order_by('-created')
		# page_number = int(self.request.GET.get('p',1))
		# paginator = Paginator(post_list, 5)
		# page_obj = paginator.get_page(page_number)
		return post_list

class PostCreateView(CreateView):
	model = Post
	template_name = 'post_create.html'
	fields = ['title', 'content']
	context_object_name = 'form'

	def form_valid(self, form):
		post = form.save(commit=False)
		# post.author =
		post.created = timezone.now()
		post.save()
		return redirect('/')

class PostEditView(UpdateView):
	model = Post
	template_name = 'post_edit.html'
	fields = ['title', 'content']
	context_object_name = 'form'
	pk_url_kwarg = 'post_id'

	def get_success_url(self,):
		return reverse('forum_app:post', kwargs={'post_id':self.object.id})


# class ComnentCreateView(CreateView):
# 	model = Comment
# 	template_name = 'post.html'
# 	fields = ['content']
# 	context_object_name = 'form'

# 	def get_queryset(self):
# 		post = get_object_or_404(Post, id=post_id)
# 		return post

# 	def form_valid(self, form):
# 		comment = form.save(commit=False)
# 		# comment.author =
# 		# comment.post = request.post
# 		comment.created = timezone.now()
# 		comment.save()
# 		return redirect('/')


def post(request, post_id):
	post = get_object_or_404(Post, id=post_id)

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			form_tmp = form.save(commit=False)
			form_tmp.post = post
			# form_tmp.author =
			form_tmp.created = timezone.now()
			form_tmp.save()
			form = form_tmp
			context = {'post':post, 'form':form}
			return redirect('/post/' + str(post_id))
	else:
		form = CommentForm()
	context = {'post':post, 'form':form}
	return render(request, 'post.html', context)
