from django.template.defaulttags import register
from django.contrib.auth.models import User
from users.models import Following


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def is_follower(maybe_follower: User, maybe_followed: User) -> bool:
    return Following.objects.filter(from_user=maybe_follower,to_user=maybe_followed).exists()
