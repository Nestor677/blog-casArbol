from django.contrib import admin
from .models import Categoria, Noticia, Comentarios, Evento

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Noticia)
admin.site.register(Comentarios)
admin.site.register(Evento)
