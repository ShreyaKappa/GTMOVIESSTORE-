from django.db import models
from django.contrib.auth.models import User
from popularity.models import Region

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username
