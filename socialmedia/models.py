from django.db import models


# How to deal with passwords in a model?
class User(models.Model):
    username = models.CharField(max_length=70)
    password = models.CharField(max_length=12)


class PostWall(models.Model):
    postContent = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
