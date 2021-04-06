from rest_framework import serializers
from rest_framework . serializers import ModelSerializer
from .models import Book
from django.contrib.auth import authenticate
from rest_framework import exceptions


class BookSerializer(ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'


class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

    def validate(self,data):
        username=data.get("username")
        password=data.get("password")

        if username and password:
            user=authenticate(username=username,password=password)
            if user:
                data["user"]=user
            else:
                msg="unable to login with given credentials"
                raise exceptions.validationError(msg)
        else:
            msg="you have to provide username and password"
            raise exceptions.validationError(msg)
        return data



        
        
        
        
        
        
        
        
        
        
        