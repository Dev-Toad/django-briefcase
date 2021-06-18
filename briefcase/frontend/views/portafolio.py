from django.shortcuts import render, HttpResponse
from ...portafolio.models import Project


def portafolio(request):
    projects = Project.objects.all()
    return render(request, "briafcase/storefront/portafolio/portafolio.html", {'projects': projects })

