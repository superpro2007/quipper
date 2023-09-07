from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect

def index_request(request: HttpRequest) -> HttpResponse:
    current_user = request.user
    if current_user.is_authenticated:
        return redirect("homepage")
    else:
        return redirect("register")
