from django.db import models
from django.utils.translation import  gettext_lazy as _

# Create your models here.
class Project(models.Model):
    title = models.CharField(
        _("Titulo"),
        max_length=200
    )
    description = models.TextField(
        _("Descripcion")
    )
    image = models.ImageField(
        _("Imagen"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = _("Proyecto")
        verbose_name_plural = _("Proyectos")
    
