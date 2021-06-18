from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "briafcase/storefront/core/home.html")


def about(request):
    return render(request, "briafcase/storefront/core/about.html")


def contact(request):
    return render(request, "briafcase/storefront/core/contact.html")


