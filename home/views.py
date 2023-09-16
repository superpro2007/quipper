from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from home.forms import NewQuipForm
from main.models import Quip
from django.contrib import messages


def home_request(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = NewQuipForm(request.POST)
        text = form.data["text"]
        quip = Quip(text=text, user=request.user)
        quip.save()
        messages.success(request, "Quip posted!")

    form = NewQuipForm()
    posts = Quip.objects.all().order_by('-id')

    return render(
        request=request,
        template_name="home.html",
        context={"new_quip_form": form, "posts": posts},
    )
