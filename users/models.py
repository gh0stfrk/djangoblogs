from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.png", upload_to="users/")

    def save(self, *args, **kwargs):
        if self.image != "default.png":
            self.image.name = f"{self.user.username}/{self.user.username}.{self.image.name.split('.')[-1]}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} Profile"
