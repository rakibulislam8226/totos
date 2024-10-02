from django.contrib import admin

from .models import Contact

# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("email", "subject", "message", "created_at")
    date_hierarchy = "created_at"
    ordering = ("-created_at",)
    readonly_fields = ("uid", "created_at", "updated_at")
    list_per_page = 25
