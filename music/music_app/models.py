from django.db import models

# Create your models here.
class Signup(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=200)
    confirm_password = models.CharField(max_length=200)

    # created_at = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.username
