from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *

class Movie_Ser(serializers.ModelSerializer):
    class Meta:
        model=Movie
        # fields="__all__"
        exclude = ['re_year']

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Add custom fields from the user model to the token response
        data.update({
            # 'user_id': self.user.id,
            'email': self.user.email,
            # add more fields as needed
        })
        
        return data