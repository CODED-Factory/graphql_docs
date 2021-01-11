from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Project


@login_required
def projects_list(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects_list.html", context)


@login_required
def voyager(request, project_slug):
    try:
        project = Project.objects.get(slug=project_slug)
    except EnvironmentError as e:
        return redirect("projects")

    context = {"api_endpoint": project.api_endpoint}
    return render(request, "voyager.html", context)
