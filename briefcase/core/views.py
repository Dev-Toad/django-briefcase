from django.shortcuts import render, HttpResponse

html_base =""" 
<h1>Mi web personal</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me/">Acerca de</a></li>
    <li><a href="/contact-me/">contacto</a></li>
    <li><a href="/portafolio-me/">portafolio</a></li>
</ul>
""" 
def home(request):
    return render(request, "frontend/templates/briefcase/core/index.html")


def about(request):
    return HttpResponse(html_base + """ 
        <h2> acerca de</h2>
        <p>Hola me llamo lardin y soy developer</p>
    """)

def contact(request):
    return HttpResponse(html_base + """
        <h2>Numero de contacto</h2>
        <p>Celular: <strong>916167489</strong></p>
    """)


def portafolio(request):
    return HttpResponse(html_base + """
        <h2>Este es mi primer portafolio</h2>
        <p><strong>skinny-dev github</strong></p>
    """)

