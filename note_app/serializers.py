from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Notes

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id','username','password','email','date_joined','updated_at']

    def create(self,validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email','')
            )
        return user
    
    def update(self,instance,validated_data):
        instance.username=validated_data.get('username',instance.username)
        instance.email=validated_data.get('email',instance.email)
        instance.save()
        return instance
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['id','title','content','last_update','created_on']
        
