from django.contrib import admin
from .models.models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
