
from django.contrib import admin
from django.urls import path
from docs.views import voyager, projects_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', projects_list, name="projects-list"),
    path('docs/<project_slug>/', voyager, name="voyager"),

]
