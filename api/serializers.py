from social.models import SocialNetwork
from rest_framework import serializers
from django.contrib.auth import get_user_model


class SocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
