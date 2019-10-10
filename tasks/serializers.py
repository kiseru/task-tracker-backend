from rest_framework import serializers

from accounts.serializers import UserSerializer
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'
