from django.urls import path

from .views import ProjectListCreateView, ProjectDetailView

urlpatterns = [
    path("/<uuid:uid>", ProjectDetailView.as_view(), name="project-detail"),
    path("", ProjectListCreateView.as_view(), name="project-list"),
]
