from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = [
        "phone",
        "email",
        "type",
    ]
    list_filter = UserAdmin.list_filter + ("status",)
    readonly_fields = ("slug",)
    ordering = ("-date_joined",)
    fieldsets = UserAdmin.fieldsets + (
        (
            "Extra Fields",
            {
                "fields": (
                    "phone",
                    "slug",
                    "image",
                    "gender",
                    "type",
                    "status",
                    "date_of_birth",
                    "height",
                    "weight",
                    "blood_group",
                    "nid",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "phone",
                )
            },
        ),
    ) + UserAdmin.add_fieldsets
