from django.urls import path, include
from .views import PostViewSet, CommentViewSet, FeedViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('posts', PostViewSet, basename='posts')
router.register('comments', CommentViewSet, basename='comments')
router.register('feed/', FeedViewSet, basename='feed')
urlpatterns = [
    path('', include(router.urls)),
   
]
