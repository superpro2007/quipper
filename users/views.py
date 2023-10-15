from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from main.models import Quip
from django.contrib.auth.models import User
from users.models import Following
from home.views import sort_posts

from .forms import NewUserForm


def register_request(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("homepage")

        messages.error(request, "Unsuccessful registration. Invalid information.")

    form = NewUserForm()

    return render(
        request=request,
        template_name="register.html",
        context={"register_form": form},
    )


def login_request(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()

    return render(
        request=request, template_name="login.html", context={"login_form": form}
    )


def logout_request(request: HttpRequest) -> HttpResponse:
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("login")


def user_profile_request(request: HttpRequest, user_id) -> HttpResponse:
    posts = Quip.objects.filter(user_id=user_id).order_by("-id")
    user_to_show = User.objects.get(id=user_id)
    parent_posts, child_posts = sort_posts(posts)

    try:
        Following.objects.get(from_user=request.user, to_user=user_to_show)
        following_exists = True
    except Following.DoesNotExist:
        following_exists = False

    followers_count = Following.objects.filter(to_user_id=user_id).count()
    followings_count = Following.objects.filter(from_user_id=user_id).count()

    return render(
        request=request,
        template_name="profile.html",
        context={
            "parent_posts": parent_posts,
            "child_posts": child_posts,
            "user_to_show": user_to_show,
            "following_exists": following_exists,
            "followers_count": followers_count,
            "followings_count": followings_count,
        },
    )


def user_follow_request(request: HttpRequest, user_to_follow_id) -> HttpResponse:
    user_to_follow = User.objects.get(id=user_to_follow_id)

    try:
        following = Following.objects.get(
            from_user=request.user, to_user=user_to_follow
        )
        following.delete()
        return HttpResponse(False)
    except Following.DoesNotExist:
        following = Following(from_user=request.user, to_user=user_to_follow)
        following.save()
        return HttpResponse(True)
