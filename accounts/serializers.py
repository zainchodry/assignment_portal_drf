from rest_framework import serializers
from . models import User



class RegisterSerializer(serializers.ModelSerializer):
    Role_Choices = [
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('teacher', 'Teacher')
    ]

    username = serializers.CharField(required = True)
    email = serializers.EmailField(required = True)
    password = serializers.CharField(write_only = True, required = True)
    confirm_password = serializers.CharField(write_only = True, required = True)
    role = serializers.ChoiceField(choices=Role_Choices, required = True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')

        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError("Email Already Exists")
        
        if password != confirm_password:
            raise serializers.ValidationError("Password Is Not Same")
        
        if not email.endswith("@gmail.com"):
            raise serializers.ValidationError("Email Must Be @gmail.com")
        
        return attrs
    

    def create(self, validated_data):
        validated_data.pop('confirm_password')

        password = validated_data.pop('password')
        user = User.objects.create_user(password=password, **validated_data)
        user.save()
        return user
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'role']

