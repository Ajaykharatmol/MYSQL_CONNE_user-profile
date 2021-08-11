from user.models import UserInfo
from rest_framework import serializers




class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'