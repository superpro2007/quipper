from django.db import models
from django.contrib.auth.models import User


class Quip(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    parent_quip = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_likes_count(self):
        likes_count = Like.objects.filter(quip_id=self.pk).count()
        return likes_count

    def __str__(self):
        return f"{self.user}: {self.text}"

    def get_replies_count(self):
        replies_count = Quip.objects.filter(parent_quip=self).count()
        return replies_count

class Like(models.Model):
    quip = models.ForeignKey(Quip, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"like of {self.user}: {self.quip.text}"

    class Meta:
        constraints = (
            models.UniqueConstraint(
                name="unique_quip_user",
                fields=["quip", "user"],
            ),
        )
