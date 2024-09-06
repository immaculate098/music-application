from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.username
    
    def get_profile_pic_url(self):
        if self.profile_pic:
            return self.profile_pic.url
        else:
            return '/path/to/default/image.jpg'
        from django.db import models

# Create your models here.
# dashboard/models.py
from django.db import models

class Search(models.Model):
    artist_name = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    search_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Search by {self.artist_name or 'Unknown Artist'}"

