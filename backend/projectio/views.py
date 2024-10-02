from rest_framework import generics

from .models import Project
from .serializers import ProjectListSerializer


# Create your views here.
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.filter()
    serializer_class = ProjectListSerializer


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.filter()
    serializer_class = ProjectListSerializer
    lookup_field = "uid"
    lookup_url_kwarg = "uid"
