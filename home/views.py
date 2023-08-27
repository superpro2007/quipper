from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def home_request(request: HttpRequest) -> HttpResponse:
    return render(
        request=request,
        template_name="home.html",
    )
