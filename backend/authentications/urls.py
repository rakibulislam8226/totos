from django.urls import path

from .views import UserAuthView, UserMeListView

urlpatterns = [
    path("/me", UserMeListView.as_view(), name="user-me"),
    path("/register", UserAuthView.as_view(), name="auth"),
]
