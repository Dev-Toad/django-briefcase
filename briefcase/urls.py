
from django.contrib import admin
from django.urls import path
from .core import views as v
urlpatterns = [
    path('', v.home, name='home'),
    path('about-me/', v.about, name="about", ),
    path('contact-me/', v.contact, name="contact", ),
    path('portafolio-me/', v.portafolio, name="portafolio", ),
    path('admin/', admin.site.urls),
]
