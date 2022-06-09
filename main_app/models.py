from django.db import models
from django.contrib.auth.models import User
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

class Comment(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment")

    def __str__(self):
        return self.title

class Piece(models.Model):
    title = models.CharField(max_length=150)
    vid = models.CharField(max_length=250)
    vid_link = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="piece")

    def __str__(self):
        return self.title

class Team(models.Model):
    name = models.CharField(max_length=150)
    about = models.TextField()
    image = models.CharField(max_length=300, default=1)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg',upload_to='profile_pics')
    bio = models.TextField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} Profile"