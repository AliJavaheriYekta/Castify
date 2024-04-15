from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email as django_default_email_validation
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from user_panel.models import CustomUser, Profile


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password])
    confirm_password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        required=True
    )

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'confirm_password', 'email', 'phone_number')
        extra_kwargs = {
            'phone_number': {'required': False}
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def validate_email(self, value):
        django_default_email_validation(value)
        if CustomUser.objects.filter(email=value).exists():
            raise ValidationError('A user with same email already exists!')
        return  value

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return CustomUser.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        if username and password:
            user = authenticate(request=self.context.get('request'), username=username, password=password)
            if user is None:
                raise serializers.ValidationError('Invalid username/password.')
            data.update({'user': user})
        else:
            raise serializers.ValidationError('Username and password are required.')
        return data


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
