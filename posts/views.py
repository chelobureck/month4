from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import randint
from posts.models import Post
from posts.forms import PostCrateForm, PostModelForm
from django.contrib.auth.decorators import login_required

def test_view(request):
    return HttpResponse(f"This is a test view {randint(1, 1000)}")

def html_view(request):
    return render(request, "base.html")

@login_required(login_url='/login/')
def list_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request, "post/list_view.html", context={"posts": posts})

@login_required(login_url='/login/')
def post_detail_view(request, post_id):
    if request.method == "GET":
        posts = Post.objects.filter(id=post_id).first()
        if not posts:
            return redirect("/posts/")
        return render(request, "post/post_detail.html", context={"post": posts})

@login_required(login_url='/login/')
def create_post_view(request):
    if request.method == "POST":
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            Post.objects.create(
                image=form.cleaned_data.get("image"),
                title=form.cleaned_data.get("title"),
                content=form.cleaned_data.get("content"),
                rate=form.cleaned_data.get("rate"),
            )
        else:
            return render(request, "post/create_post.html", context={"form": form})
        return redirect("/list_view/")
    if request.method == "GET":
        return render(request, "post/create_post.html")