from django.contrib import admin
from .models import Project

# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "start_date", "end_date", "status"]
    list_filter = ["status"]
    readonly_fields = ["uid", "created_at", "updated_at"]
    date_hierarchy = "created_at"
    list_per_page = 50
