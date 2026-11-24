from rest_framework import serializers
from .managers import UserManager
from .models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'full_name', 'password', 'password_confirm']
        extra_kwargs = {  "password": {"write_only": True, },
                          "password_confirm": {"write_only": True,}
                        }
        
    def validate(self, attrs):
        if attrs['password'] == attrs['password_confirm']:
            return attrs
        else:
            raise serializers.ValidationError("Passwords do not match")
        
    def validate_password(self, value):
        validate_password(value)
        return value
    
    def create(self, validated_data):
        password = validated_data["password"]
        email = validated_data["email"]
        validated_data.pop("password_confirm")
        return User.objects.create_user(**validated_data)
    
class UserSerializer(serializers.ModelSerializer):
    primary_department = serializers.StringRelatedField()
    
    class Meta:
        model = User
        fields = ['id', 'email', 'full_name', 'primary_department', 'role', 'clearance_level']
        
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = UserSerializer(self.user).data
        return data
        