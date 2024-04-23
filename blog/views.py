from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Post, Like, Comments


def home(request):
    posts = Post.objects.all().order_by("-date_posted")
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {"post": post, "request": request}
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
