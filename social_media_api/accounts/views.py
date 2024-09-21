
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework import generics
from .serializers import CustomUserSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # This creates the user and generates a token
            token = Token.objects.get(user=user)  # Retrieve the created token
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            # Authentication logic here
            return Response("Login successful")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

User = get_user_model()

# View to list all users
class UserListView(generics.GenericAPIView):
    queryset = User.objects.all()  # Equivalent to CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]  # Ensures only authenticated users can access this view

    def get(self, request, *args, **kwargs):
        users = self.get_queryset()
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)


# View for following a user
class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            user_to_follow = User.objects.get(id=kwargs.get('user_id'))
            request.user.following.add(user_to_follow)
            return Response({'status': 'User followed'}, status=200)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)


# View for unfollowing a user
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            user_to_unfollow = User.objects.get(id=kwargs.get('user_id'))
            request.user.following.remove(user_to_unfollow)
            return Response({'status': 'User unfollowed'}, status=200)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
