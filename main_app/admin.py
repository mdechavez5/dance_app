from django.contrib import admin
from .models import Profile, Post, Piece, Team, Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Piece)
admin.site.register(Team)
admin.site.register(Comment)