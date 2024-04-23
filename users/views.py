from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from .forms import UserRegisterForm, UploadProfilePhotoForm, UpdateUserForm
from .models import Profile
from django.shortcuts import get_object_or_404


def user_profile(request: HttpRequest, username: str):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    return JsonResponse(
        {
            "user": {"username": user.username, "email": user.email},
            "profile": {"image": str(profile.image.url)},
        }
    )


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your account has been created. You can now login"
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


def update_user(request):
    user_obj = get_object_or_404(User, id=request.user.id)
    if request.method == "POST":
        form = UpdateUserForm(request.POST, instance=user_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been updated.")
            return redirect("profile")


def handle_profile_photo(user, profile_photo):
    profile = Profile.objects.get(user=user)
    profile.image = profile_photo
    profile.save()


@login_required
def profile(request: HttpRequest):
    if request.method == "POST":
        form = UploadProfilePhotoForm(request.POST, request.FILES)
        if form.is_valid():
            profile_photo = request.FILES["image"]
            handle_profile_photo(request.user, profile_photo)
    form = UploadProfilePhotoForm()
    update_user = UpdateUserForm(instance=request.user)

    return render(
        request, "users/profile.html", {"form": form, "userform": update_user}
    )
