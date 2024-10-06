from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "phone",
            "first_name",
            "last_name",
            "nid",
            "image",
            "type",
            "status",
            "gender",
            "date_of_birth",
            "height",
            "weight",
            "blood_group",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = User(
            email=validated_data["email"],
            phone=validated_data["phone"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            nid=validated_data["nid"],
            image=validated_data.get("image"),
            type=validated_data.get("type"),
            status=validated_data.get("status"),
            gender=validated_data.get("gender"),
            date_of_birth=validated_data.get("date_of_birth"),
            height=validated_data.get("height"),
            weight=validated_data.get("weight"),
            blood_group=validated_data.get("blood_group"),
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
