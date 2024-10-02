from rest_framework import serializers 
from .models import Task, CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user
        return super(TaskSerializer, self).create(validated_data)    