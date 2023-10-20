from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    id= serializers.ReadOnlyField()
    first_name= serializers.CharField()
    last_name= serializers.CharField()
    username= serializers.CharField()
    email= serializers.EmailField()
    password= serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password']

    def create(self, validated_data):
        instance= User()
        instance.first_name= validated_data.get('first_name')
        instance.last_name= validated_data.get('last_name')
        instance.username= validated_data.get('username')
        instance.email= validated_data.get('email')
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value
