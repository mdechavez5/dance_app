from django.contrib import admin
from .models import Profile, Post, Piece, Team

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Piece)
admin.site.register(Team)