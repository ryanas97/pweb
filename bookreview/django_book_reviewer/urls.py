"""Sets up URL configurations for each application belonging to this project."""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include("apps.reviewer.urls")),
]
