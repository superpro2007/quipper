from django.db import models
from django.contrib.auth.models import User
from django.db.models import UniqueConstraint
from django.db.models.signals import post_save
from django.dispatch import receiver


class Following(models.Model):
    from_user = models.ForeignKey(
        User, null=False, on_delete=models.CASCADE, related_name="from_following"
    )
    to_user = models.ForeignKey(
        User, null=False, on_delete=models.CASCADE, related_name="to_following"
    )

    def __str__(self):
        return f"{self.from_user} follows {self.to_user}"

    class Meta:
        constraints = (
            UniqueConstraint(
                name="unique_from_user_to_user",
                fields=["from_user", "to_user"],
            ),
        )


class Quipper(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def get_followings_count(self) -> int:
        return Following.objects.filter(from_user_id=self.user.pk).count()

    def get_followers_count(self) -> int:
        return Following.objects.filter(to_user_id=self.user.pk).count()

    def get_userpic_color(self):
        saturation = 30
        lightness = 80
        hash_val = 0
        
        for char in self.user.username:
            hash_val = ord(char) + ((hash_val << 5) - hash_val)

        h = hash_val % 360
        return 'hsl({}, {}%, {}%)'.format(h, saturation, lightness)



@receiver(post_save, sender=User)
def valid_order(sender, instance: User, **kwargs):
    if not Quipper.objects.filter(user=instance).exists():
        quipper = Quipper(user=instance)
        quipper.save()
