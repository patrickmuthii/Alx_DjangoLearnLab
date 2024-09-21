from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django_filters import rest_framework as filters
# Create your views here.

class PostFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    content = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['title', 'content']
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class =PostFilter
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise Exception('You do not have permission to edit this post')
        serializer.save()    

    def perform_destroy(self, serializer):
        if serializer.instance.author != self.request.user:
            raise Exception('You do not have permission to delete this post')
        serializer.save()    

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise Exception('You do not have permission to edit this comment')
        serializer.save()

    
    def perform_destroy(self, serializer):
        if serializer.instance.author != self.request.user:
            raise Exception('You do not have permission to delete this comment')
        serializer.destroy()
                

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()

class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get the list of users the current user is following
        following_users = request.user.following.all()

        # Fetch posts made by the followed users, ordered by creation date
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        # Serialize the posts (you'll need to create a PostSerializer)
        from .serializers import PostSerializer
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    