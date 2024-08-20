from django.contrib.auth.hashers import make_password, check_password
from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class Signup(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=200)
    confirm_password = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:  # Ensures this only runs on creation
            self.password = make_password(self.password)  # Hash the password
        super(Signup, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
