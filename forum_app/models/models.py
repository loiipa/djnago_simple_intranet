from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=64)
	# author = models.ForeignKey(User, on_delete=models.CASCADE)
	author = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
	content = models.TextField()
	created = models.DateTimeField()

	def __str__(self):
		return self.title

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	# author = models.ForeignKey(User, on_delete=models.CASCADE)
	author = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
	content = models.TextField()
	created = models.DateTimeField()

	def __str__(self):
		return self.post
