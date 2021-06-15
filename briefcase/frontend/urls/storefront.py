from django.urls import path

from ..views.core import home, about, contact, portafolio

urlpatterns = [
    path(
        "",
        home,
        name="home"
    ),
    path(
        "about",
        about,
        name="about"
    ),
    path(
        "contact",
        contact,
        name="contact"
    ),
    path(
        "portafolio",
        portafolio,
        name="portafolio"
    )
]