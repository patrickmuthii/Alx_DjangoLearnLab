from django.db import models

# Create your models here.

class Notification(models.Model):
    recipient = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    actor = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    target = models.ForeignKey('posts.Post', on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.recipient} {self.verb} {self.target}'