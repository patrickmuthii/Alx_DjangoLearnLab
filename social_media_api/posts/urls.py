from django.urls import path, include
from .views import PostViewSet, CommentViewSet, FeedView, LikePostView, UnlikePostView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('posts', PostViewSet, basename='posts')
router.register('comments', CommentViewSet, basename='comments')
router.register('feed/', FeedView, basename='feed')
router.register('posts/<int:post_id>/like', LikePostView, basename='like')
router.register('posts/<int:post_id>/unlike', UnlikePostView, basename='unlike')
urlpatterns = [
    path('', include(router.urls)),
   
]
