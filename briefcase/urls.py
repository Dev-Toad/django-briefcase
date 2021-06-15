
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .core import views as v

from .frontend import urls as frontend_urls
urlpatterns = [
    path("", include(frontend_urls)),
]

