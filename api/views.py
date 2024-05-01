from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics

from .serializers import MyTokenObtainPairSerializer, SocialNetworkSerializer, RegisterSerializer
from social.models import SocialNetwork
from . import utils


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny, )


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def get_social_networks(request):
    if request.method == 'GET':
        social_networks = utils.get_social_network_by_filter(user_id=request.user.id)
        serializer = SocialNetworkSerializer(social_networks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = SocialNetworkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class SocialNetworkDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SocialNetworkSerializer
    queryset = SocialNetwork.objects.all()
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        if utils.is_author(self.get_object(), request.user.id):
            return super().put(request, *args, **kwargs)
        return Response({'message': 'Ошибка доступа'})
    

# Создал endpoint SocialNetworkDetail и удалил запросы к бд