from django.contrib import admin
from posts.models import Comment, Post, Tag, Category


admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)