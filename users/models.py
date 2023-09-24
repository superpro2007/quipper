from django.db import models
from django.contrib.auth.models import User
from django.db.models import UniqueConstraint


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
