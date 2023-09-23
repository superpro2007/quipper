from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from main.models import Quip, Like
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def index_request(request: HttpRequest) -> HttpResponse:
    return redirect("homepage")


@login_required
def quip_like_request(request: HttpRequest, quip_id) -> HttpResponse:
    if request.method == "POST":
        quip = Quip.objects.get(id=quip_id)
        try:
            like = Like.objects.get(quip=quip, user=request.user)
            like.delete()
        except Like.DoesNotExist:
            like = Like(quip=quip, user=request.user)
            like.save()
            messages.success(request, "Liked!")

    return redirect("homepage")
