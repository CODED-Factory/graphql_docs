from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    readonly_fields = ["slug"]
