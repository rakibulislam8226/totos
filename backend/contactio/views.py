from django.shortcuts import render
from rest_framework import generics, permissions

from .serializers import ContactListSerializer
from .models import Contact

# Create your views here.


class ContactListView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializer
    permission_classes = [permissions.AllowAny]
