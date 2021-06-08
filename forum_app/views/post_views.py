from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from forum_app.forms.forms import PostForm, CommentForm
from forum_app.models.models import Post, Comment
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, reverse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
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

class PostCreateView(LoginRequiredMixin, CreateView):
	login_url = '/login/'
	redirect_field_name = 'login'
	model = Post
	template_name = 'post_edit.html'
	fields = ['title', 'content']
	context_object_name = 'form'

	def form_valid(self, form):
		post = form.save(commit=False)
		post.author = self.request.user
		post.created = timezone.now()
		post.save()
		return redirect('/')

class PostEditView(LoginRequiredMixin, UpdateView):
	login_url = '/login/'
	redirect_field_name = 'login'
	model = Post
	template_name = 'post_edit.html'
	fields = ['title', 'content']
	context_object_name = 'form'
	pk_url_kwarg = 'post_id'

	def get_success_url(self):
		return reverse('forum_app:post', kwargs={'post_id':self.object.id})

class PostDeleteView(LoginRequiredMixin, DeleteView):
	login_url = '/login/'
	redirect_field_name = 'login'
	model = Post
	template_name = 'post_delete.html'
	context_object_name = 'post'
	pk_url_kwarg = 'post_id'

	def get_success_url(self):
		return reverse('forum_app:home')

# class CommentDeleteView(LoginRequiredMixin, DeleteView):
# 	login_url = '/login/'
# 	redirect_field_name = 'login'
# 	model = Comment
# 	template_name = 'comment_delete.html'
# 	context_object_name = 'comment'
# 	pk_url_kwarg = 'post_id'

# 	def get_success_url(self):
# 		return reverse('forum_app:post', kwargs={'post_id':self.object.id})

@login_required(login_url='forum_app:login')
def post(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	print(post)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			form_tmp = form.save(commit=False)
			form_tmp.post = post
			form_tmp.author = request.user
			form_tmp.created = timezone.now()
			form_tmp.save()
			form = form_tmp
			context = {'post':post, 'form':form}
			return redirect('/post/' + str(post_id))
	else:
		form = CommentForm()
	context = {'post':post, 'form':form}
	return render(request, 'post.html', context)

@login_required(login_url='forum_app:login')
def post_2(request, post_id, com_id):
	post = get_object_or_404(Post, pk=post_id)
	comment = get_object_or_404(Comment, pk=com_id)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			form_tmp = form.save(commit=False)
			# form_tmp.post = post
			form_tmp.parent_comment = comment
			form_tmp.author = request.user
			form_tmp.created = timezone.now()
			form_tmp.save()
			form = form_tmp
			context = {'post':post, 'form':form}
			return redirect('/post/' + str(post_id))
	else:
		form = CommentForm()
	context = {'post':post, 'form':form, 'com':comment}
	return render(request, 'post_2.html', context)
