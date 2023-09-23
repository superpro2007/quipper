from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from main.models import Quip, Like
from django.contrib.auth.decorators import login_required


@login_required
def index_request(request: HttpRequest) -> HttpResponse:
    return redirect("homepage")


def quip_like_request(request: HttpRequest, quip_id) -> HttpResponse:
    quip = Quip.objects.get(id=quip_id)

    try:
        like = Like.objects.get(quip=quip, user=request.user)
        like.delete()
    except Like.DoesNotExist:
        like = Like(quip=quip, user=request.user)
        like.save()

    return HttpResponse(quip.get_likes_count())
