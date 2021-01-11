
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from docs.views import voyager, projects_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', projects_list, name="projects-list"),
    path('docs/<project_slug>/', voyager, name="voyager"),

]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)