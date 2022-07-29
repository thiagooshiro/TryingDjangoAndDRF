from django.shortcuts import render
from django.http import JsonResponse
from socialmedia.models import User, PostWall
from config.serializers import PostSerializer, UserSerializer
# Create your views here.
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


def index(request):
    return HttpResponse("Hello, World, you're at socialmedia index")


class UserViews():
    def get_users_info(request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse({ "users": serializer.data })

    @api_view(['GET'])
    def get_user_info(request, id):
        try:
            user = User.objects.get(pk = id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)   
        
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    @api_view(['POST'])
    def create_user(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @api_view(['PUT'])
    def edit_user(request, id):
        try:
            user = User.objects.get(pk = id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['DELETE'])
    def destroy_user(request, id):
        try:
            user = User.objects.get(pk = id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class WallRequests():

    @api_view(['GET'])
    def retrieve_posts(request):
        wall_posts = PostWall.objects.all()
        serializer = PostSerializer(wall_posts, many=True)
        return Response(serializer.data)

    @api_view(['GET'])
    def wall_post_details(request, id):
        try:
            wall_post = PostWall.objects.get(pk = id)
        except PostWall.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)   
        serializer = PostSerializer(wall_post)
        return Response(serializer.data)

    @api_view(['POST'])
    def create_post(request):
        print(request.user)
        print(request.method)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
