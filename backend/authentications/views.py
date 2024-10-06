from rest_framework import generics, permissions, status, views
from rest_framework.response import Response

from .serializers import UserSerializer


class UserAuthView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
