from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        User = get_user_model()
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        User = get_user_model()
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        User = get_user_model()
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        Token.objects.create(user=user)
        return user
