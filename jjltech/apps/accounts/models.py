from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = CountryField(blank_label='(select country)', default='NG')
    headline = models.CharField(max_length=150, blank=True)
    profile_image = models.ImageField(upload_to='profile_pics/', blank=True)
    bio = models.TextField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.profile_image:
            # Get the file extension
            ext = os.path.splitext(self.profile_image.name)[1]
            # Rename the file to the user's username
            new_filename = f"{self.user.username}{ext}"
            # Save the file with the new name
            self.profile_image.name = f"{new_filename}"

        if self.profile_image:
            print(f"Saving file to: {self.profile_image.name}")

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}'s Profile"

