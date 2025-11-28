from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import randint
from posts.models import Post

def test_view(request):
    return HttpResponse(f"This is a test view {randint(1, 1000)}")

def html_view(request):
    return render(request, "base.html")

def view_posts(request):
    posts = Post.objects.all()
    return render(request, "post/posts_view.html", context={"posts": posts})