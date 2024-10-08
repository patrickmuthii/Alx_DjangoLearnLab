from rest_framework import serializers 
from .models import Task, CustomUser

# Serializers
# A Serialrizer for user model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

# Serialrizer for task model
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

# these overides the default create method when the create method is called from the view
    
    def create(self, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user
        return super(TaskSerializer, self).create(validated_data)    