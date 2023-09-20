from django.db import models
from django.contrib.auth.models import User
from django.db.models import UniqueConstraint


class Quip(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.user}: {self.text}"


class Like(models.Model):
    quip = models.ForeignKey(Quip, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"like of {self.user}: {self.quip.text}"

    class Meta:
        constraints = (
            UniqueConstraint(
                name="unique_quip_user",
                fields=["quip", "user"],
            ),
        )
