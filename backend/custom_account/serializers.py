from rest_framework import serializers
from .models import CustomUser


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True,style={'input_type': 'password'})
    
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'password2', 'username', 'first_name')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        password2 = validated_data.pop('password2',None)
        instance = self.Meta.model(**validated_data)
        if password != password2:
            raise serializers.ValidationError('both passwords must be same')
            return
        instance.set_password(password)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email','username','first_name','is_staff','is_active','date_joined')
