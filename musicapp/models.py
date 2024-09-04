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
from django.db import models
from django.contrib.auth.models import User

# class Comment(models.Model):
#     artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'Comment by {self.user} on {self.artist}'
