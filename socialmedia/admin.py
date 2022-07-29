from django.contrib import admin

# Register your models here.

from .models import User, PostWall

admin.site.register(User)
admin.site.register(PostWall)
