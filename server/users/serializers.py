from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'last_login', 'is_superuser', 'is_active', 'date_joined']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        email = validated_data.pop('email', None)
        password = validated_data.pop('password', None)
        
        user = self.Meta.model(**validated_data)

        if email is not None:
            user.email = email.lower()

        if password is not None:
            user.set_password(password)

        user.save()
        return user