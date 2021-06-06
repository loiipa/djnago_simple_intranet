from django.shortcuts import render, get_object_or_404
from forum_app.models import Post
from forum_app.forms import UserForm, PostForm, CommentForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def home(request):
	user_name = 'Guest'
	user = ''

	post_list = Post.objects.order_by('-created')
	context = {'post_list':post_list, 'user_name':user_name, 'user':user}

	return render(request, 'home.html', context)

def registration(request):
	user_name = 'Guest'

	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			user_name = request.POST.get('username')
			return redirect('/')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	else:
		form = UserForm()
	return render(request, 'registration.html', {'user_name':user_name, 'form':form})

def login_request(request):
	user_name = 'Guest'
	username = ''
	notice = ''

	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				user_name = request.POST.get('username')
				return redirect('/')
			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")
	else:
		form = UserForm()

	return render(request, 'login.html', {'user_name':user_name, 'form':form, 'notice':notice})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect('/')

def post(request, post_id):
	post =  get_object_or_404(Post, id=post_id)
	context = {'post':post}
	return render(request, 'post.html', context)
