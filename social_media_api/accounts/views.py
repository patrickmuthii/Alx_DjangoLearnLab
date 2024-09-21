
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import UserRegistrationSerializer, UserLoginSerializer

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
    
class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]
    
    User = get_user_model()

    def post(self, request, user_id):
        try:
            user = self.User.objects.get(id=user_id)
        except self.User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        if user == request.user:
            return Response({"error": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)

        if user in request.user.following.all():
            request.user.following.remove(user)
            return Response({"message": "User unfollowed successfully"}, status=status.HTTP_200_OK)
        else:
            request.user.following.add(user)
            return Response({"message": "User followed successfully"}, status=status.HTTP_200_OK)
        
class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]
    
    User = get_user_model()

    def post(self, request, user_id):
        try:
            user = self.User.objects.get(id=user_id)
        except self.User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        if user == request.user:
            return Response({"error": "You cannot unfollow yourself"}, status=status.HTTP_400_BAD_REQUEST)

        if user in request.user.following.all():
            request.user.following.remove(user)
            return Response({"message": "User unfollowed successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "User is not followed"}, status=status.HTTP_400_BAD_REQUEST)
        #    