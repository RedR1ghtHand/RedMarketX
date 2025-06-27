from rest_framework import serializers
from account.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'mc_username', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
