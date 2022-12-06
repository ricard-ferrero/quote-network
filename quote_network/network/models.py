from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    quote = models.CharField(max_length=500)
    author_quote = models.CharField(max_length=100)

    def __str__(self):
        return f'Profile: {self.user.username}'