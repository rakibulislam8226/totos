from rest_framework import generics, permissions

from .serializers import UserSerializer


class UserAuthView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserMeListView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user if self.request.user.is_authenticated else None
