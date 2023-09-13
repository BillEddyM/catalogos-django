from django.contrib import admin
from .models import Pais, Departamento, Municipio

# Register your models here.
admin.site.register(Pais)
admin.site.register(Departamento)
admin.site.register(Municipio)
