from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import randint
from posts.models import Post

def test_view(request):
    return HttpResponse(f"This is a test view {randint(1, 1000)}")

def html_view(request):
    return render(request, "base.html")

def list_view(request):
    posts = Post.objects.all()
    return render(request, "post/list_view.html", context={"posts": posts})

def post_detail_view(request, post_id):
    posts = Post.objects.filter(id=post_id).first()
    if not posts:
        return redirect("/posts/")
    return render(request, "post/post_detail.html", context={"post": posts})