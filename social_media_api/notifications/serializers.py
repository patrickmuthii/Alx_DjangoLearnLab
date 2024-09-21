from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    sender_username = serializers.CharField(source='sender.username', read_only=True)
    post_title = serializers.CharField(source='post.title', read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'sender_username', 'notification_type', 'post_title', 'is_read', 'timestamp']
        read_only_fields = ['recipient', 'sender', 'notification_type', 'post', 'timestamp']
