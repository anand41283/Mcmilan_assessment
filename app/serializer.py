from rest_framework import serializers
from app.models import *
from django.contrib.auth.models import User

class Userregistration(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']

class Login(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()    

class Deptserializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields="__all__"   

class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"        
