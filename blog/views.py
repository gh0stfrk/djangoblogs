
from django.contrib import messages
from django.http import HttpRequest, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm, PostComment
from .models import Post, Like, Comments
import json


def home(request):
    posts = Post.objects.all().order_by("-date_posted")
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def add_comment(request: HttpRequest):
    comment_form = PostComment(request.POST)
    if comment_form.is_valid():
        content = comment_form.cleaned_data["content"]
        post_id = request.POST.get("post")
        try:
            post = Post.objects.get(pk=post_id)
            comment = Comments(
            content=content,
            user=request.user,
            post=post
            )
            comment.save()
            return redirect("detail", pk=comment.post.pk)
        except:
            messages.error(request, "Post not found")
            return redirect("blog-home")

def like_a_post(request: HttpRequest):
    if request.user.is_authenticated and request.method == "POST":
        body_d = json.loads(request.body.decode("utf-8"))
        post_id = body_d["post_id"]
        post = Post.objects.get(pk=post_id)
        post.like.number += 1
        post.like.save()
        current_likes = post.like.number
        return JsonResponse({"likes": current_likes})
    return JsonResponse({"error": "Must be logged in to like a post"})


def about(request):
    return render(request, "blog/about.html", {"title": "About"})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = PostComment()
    context = {"post": post, "request": request, "comment_form": comment_form}
    return render(request, "blog/post_detail.html", context)


def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        if request.user == post.author or request.user.is_superuser:
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                user = form.save(commit=False)
                user.save()
                messages.success(request, "The post has been updated successfully.")
                return redirect("blog-home")
            else:
                messages.error(request, "Please correct the following errors:")
        messages.error(request, "You are not authorized to update this post.")
    else:
        form = PostForm(instance=post)
    return render(request, "blog/create_post.html", {"form": form, "type": "Update"})


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            user.save()
            messages.success(request, "The post has been created successfully.")
            return redirect("blog-home")
        else:
            messages.error(request, "Please correct the following errors:")
    else:
        form = PostForm()
    return render(request, "blog/create_post.html", {"form": form, "type": "Create"})
