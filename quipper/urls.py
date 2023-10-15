from django.contrib import admin
from django.urls import path
from users.views import (
    register_request,
    login_request,
    logout_request,
    user_profile_request,
    user_follow_request,
    user_followings,
    user_followers,
)
from home.views import home_request, quip_details_request
from main.views import index_request, quip_like_request

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register", register_request, name="register"),
    path("home", home_request, name="homepage"),
    path("login", login_request, name="login"),
    path("logout", logout_request, name="logout"),
    path("", index_request, name="index"),
    path("quip/<quip_id>/like", quip_like_request, name="quip_like"),
    path("user/<user_id>", user_profile_request, name="user_profile"),
    path("user/<user_to_follow_id>/follow", user_follow_request, name="user_follow"),
    path("quip/<quip_id>", quip_details_request, name="quip_details"),
    path("user/<user_id>/followings", user_followings, name="user_followings"),
    path("user/<user_id>/followers", user_followers, name="user_followers"),

]
