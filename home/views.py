from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from home.forms import NewQuipForm


def home_request(request: HttpRequest) -> HttpResponse:
    form = NewQuipForm()
    return render(
        request=request,
        template_name="home.html",
        context={"new_quip_form": form},
    )
