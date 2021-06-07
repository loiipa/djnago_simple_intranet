from django.contrib import admin
from forum_app.models.models import Post, Comment
from forum_app.models.profile_models import Profile

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profile)
