from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from home.forms import NewQuipForm
from main.models import Quip
from users.models import Following
from django.contrib import messages
from django.contrib.auth.decorators import login_required

FOLLOWING = "following"
FOR_YOU = "for_you"
TIMELINE = "timeline"


@login_required
def home_request(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = NewQuipForm(request.POST)
        text = form.data["text"]
        quip = Quip(text=text, user=request.user)
        quip.save()
        messages.success(request, "Quip posted!")

    timeline = request.GET.get(TIMELINE, request.session.get(TIMELINE, FOR_YOU))
    request.session[TIMELINE] = timeline

    form = NewQuipForm()
    posts = get_posts(timeline, request.user)
    return render(
        request=request,
        template_name="home.html",
        context={"new_quip_form": form, "posts": posts, "timeline": timeline},
    )


def get_posts(timeline_mode, user):
    if timeline_mode == FOR_YOU:
        return Quip.objects.all().order_by("-id")
    else:
        followings = Following.objects.filter(from_user=user)
        followed_users = list(map(lambda following: following.to_user, followings))
        followed_users.append(user)
        return Quip.objects.filter(user__in=followed_users).order_by("-id")


@login_required
def quip_details_request(request: HttpRequest, quip_id) -> HttpResponse:
    post = Quip.objects.get(id=quip_id)

    if request.method == "POST":
        form = NewQuipForm(request.POST)
        text = form.data["text"]
        quip = Quip(text=text, user=request.user, parent_quip=post)
        quip.save()
        messages.success(request, "Quip posted!")

    form = NewQuipForm()
    form.fields["text"].widget.attrs["placeholder"] = "Put your reply here!"
    child_posts = Quip.objects.filter(parent_quip=post).order_by("-id")

    return render(
        request=request,
        template_name="quip.html",
        context={"post": post, "new_quip_form": form, "posts": child_posts},
    )
