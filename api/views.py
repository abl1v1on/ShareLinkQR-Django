from django.contrib.auth import get_user_model
from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import generics, mixins

from .serializers import SocialNetworkSerializer, UserSerializer
from social.models import SocialNetwork


class SocialNetworksListAPIView(generics.ListCreateAPIView):
    queryset = SocialNetwork.objects.all()
    serializer_class = SocialNetworkSerializer


@api_view(['GET', 'POST'])
def get_user_social_networks(request, user_id):
    if request.method == 'GET':
        social_networks = SocialNetwork.objects.filter(user_id=user_id)
        if social_networks.exists():
            serializer = SocialNetworkSerializer(social_networks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        serializer = SocialNetworkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

