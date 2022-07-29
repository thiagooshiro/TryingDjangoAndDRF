from rest_framework import serializers
from  socialmedia.models import User, PostWall


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'id', 'username', ]

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostWall
        fields = [ 'id', 'postContent', 'user_id']