from rest_framework import serializers
from rest_framework import serializers
from .models import CustomUser

class  UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [  'username', 'first_name', 'last_name', 'age', 'email', 'phone', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = CustomUser(**validated_data)
        if password is not None:
            user.set_password(password)  
        user.save()
        return user
 
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)  
        instance = super().update(instance, validated_data)   
        if password:
            instance.set_password(password)
            instance.save()
        
        return instance