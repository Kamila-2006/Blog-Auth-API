from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile-images/', blank=True, null=True)
    #website =