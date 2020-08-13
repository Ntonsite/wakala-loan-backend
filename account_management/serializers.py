from rest_framework import serializers
from account_management.models import User,Role


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'middle_name', 'last_name',
                  'email', 'username', 'roles')

    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
            email=validated_data['email'],
            username=validated_data['username'],
            password=f"{validated_data['phone']}.{validated_data['first_name']}"
        )
        user.save(force_insert=True)
        return user


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('__all__')
