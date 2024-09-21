from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token



from django.contrib.auth import get_user_model
from rest_framework import serializers

# Get the custom user model
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

# Get the custom user model
User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password_confirm = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User  # Use the custom user model
        fields = ['username', 'email', 'password', 'password_confirm', 'bio', 'profile_picture']

    def validate(self, data):
        # Ensure passwords match
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords must match.")
        return data

    def create(self, validated_data):
        # Remove the password_confirm field as it's not needed for user creation
        validated_data.pop('password_confirm')
        # Use create_user from the custom user model to create the user
        user = User.objects.create_user(**validated_data)
        # Create a token for the new user
        Token.objects.create(user=user)
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
