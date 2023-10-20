from django.contrib.auth.models import User
from .models import Contact
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'user', 'first_name', 'last_name', 'phone_number')

    def validate_first_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError(
                "First name must be at least 2 characters long.")
        return value

    def validate_last_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError(
                "Last name must be at least 2 characters long.")
        return value

    def validate_phone_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError(
                "Phone number must contain only digits.")
        if len(value) < 10:
            raise serializers.ValidationError(
                "Phone number must be at least 10 digits long.")
        return value

    def validate(self, data):
        return data
