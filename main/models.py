from django.db import models
from django.contrib.auth.models import User



class Quip(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.user}: {self.text}'
