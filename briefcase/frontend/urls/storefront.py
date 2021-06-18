from django.urls import path

# from ..views.core import home, about, contact, portafolio
from ..views import core, portafolio
urlpatterns = [
    path(
        "",
        core.home,
        name="home"
    ),
    path(
        "about",
        core.about,
        name="about"
    ),
    path(
        "contact",
        core.contact,
        name="contact"
    ),
    path(
        "portafolio",
        portafolio.portafolio,
        name="portafolio"
    )
]