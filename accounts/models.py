from django.contrib.auth.models import User
from django.db import models


# ---------------Profile---------------------------------------------
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_image = models.ImageField(null=True, blank=True, upload_to='media/images/profile_images')



    def __str__(self):
        return str(self.user)