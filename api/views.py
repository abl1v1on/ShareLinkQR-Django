from django.contrib.auth import get_user_model
from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import generics, mixins

from .serializers import SocialNetworkSerializer, UserSerializer
from social.models import SocialNetwork


