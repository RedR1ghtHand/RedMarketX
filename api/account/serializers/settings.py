from rest_framework import serializers
from account.models import User


class McUsernameUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['mc_username']


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, min_length=8)