from django.urls import path

from . import views

from .views import UserViews, WallRequests

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('users', UserViews.get_users_info),
    path('users/<int:id>', UserViews.get_user_info),
    path('users/<int:id>/edit', UserViews.edit_user),
    path('users/create', UserViews.create_user),
    path('users/<int:id>/destroy', UserViews.destroy_user),
    # fazer urls separados entre Wall e User?
    path('posts/<int:id>', WallRequests.wall_post_details),
    path('posts', WallRequests.retrieve_posts),
    path('posts/create', WallRequests.create_post)
]