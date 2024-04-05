from rest_framework import serializers
from .models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        groups = validated_data.pop("groups")
        permissions = validated_data.pop("user_permissions")

        user = User.objects.create_user(**validated_data)
        
        user.groups.set(groups)
        user.user_permissions.set(permissions)

        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", False)
        
        instance = super().update(instance, validated_data)

        if password:
            instance.set_password(password)
            instance.save() 

        return instance

