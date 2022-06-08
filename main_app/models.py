from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
from django.forms import CharField
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date_posted']

class Piece(models.Model):
    title = models.CharField(max_length=150)
    vid = models.CharField(max_length=250)
    vid_link = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="piece")

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg',upload_to='profile_pics')
    bio = models.TextField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} Profile"

# class CustomUser(AbstractUser):
#     mobile_no = models.IntegerField(blank=True,null=True)
#     date_of_birth = models.DateField(blank=True,null=True)