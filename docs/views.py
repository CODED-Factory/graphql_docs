from django.shortcuts import render, redirect
from .models import Project


def projects_list(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects_list.html", context)


def voyager(request, project_slug):
    try:
        project = Project.objects.get(slug=project_slug)
    except EnvironmentError as e:
        return redirect("projects")

    context = {"api_endpoint": project.api_endpoint}
    return render(request, "voyager.html", context)
