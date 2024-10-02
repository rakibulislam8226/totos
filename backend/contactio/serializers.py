from rest_framework import serializers

from .models import Contact


class ContactListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            "id",
            "uid",
            "email",
            "subject",
            "message",
            "created_at",
            "updated_at",
        ]
