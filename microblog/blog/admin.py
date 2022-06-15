from django.contrib import admin

from blog.models import Post
from .models import Post, Comment #models.pyで作ったPostを呼び出す


# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)