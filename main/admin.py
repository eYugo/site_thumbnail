from django.contrib import admin
from .models import Post, Thumbnail, Vote

admin.site.register(Post)
admin.site.register(Thumbnail)
admin.site.register(Vote)
