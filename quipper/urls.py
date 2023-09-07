from django.contrib import admin
from django.urls import path
from users.views import register_request, login_request, logout_request
from home.views import home_request
from main.views import index_request

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register", register_request, name="register"),
    path("home", home_request, name="homepage"),
    path("login", login_request, name="login"),
    path("logout", logout_request, name= "logout"),
    path("",index_request, name= "index"),

]
