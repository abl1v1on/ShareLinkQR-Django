from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from social.models import SocialNetwork


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token
    

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True
    )
    email = serializers.EmailField(
        write_only=True,
        required=True
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'password2']
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {'password': 'Пароли не совпадают'}
            )

        email = attrs['email']
        if get_user_model().objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': 'Пользователь с таким email уже существует'}
        )
        return attrs
    
    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class SocialNetworkSerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()
    
    class Meta:
        model = SocialNetwork
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'] = UserSerializer(read_only=True)
    
    def get_icon(self, obj):
        return f'/static/images/{obj.name}.png'

    def create(self, validated_data):
        user = get_user_model().objects.get(pk=validated_data['user_id'])
        if user.social_networks.filter(name=validated_data['name']).exists():
            raise serializers.ValidationError({'message': 'Социальная сеть уже существует'})
        return super().create(validated_data)
