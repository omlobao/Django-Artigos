from django.contrib import admin
from .models import Autor, EixoTecnologia, Artigo

@admin.register(Autor)
class AutorAadmin(admin.ModelAdmin):
    list_display = ("nome", "biografia", "email",)
    search_fields = ("nome", "biografia", "email",)
    list_filter = ("nome",)


@admin.register(EixoTecnologia)
class EixoTecnologiaAdmin(admin.ModelAdmin):
    list_display = ("nome", "Autor")
    search_fields = ("nome", "Autor")
    list_filter = ('nome',)


@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('texto', 'id_fk_eixo', 'id_fk_autor')
    search_fields = ('texto',)
    list_filter = ('texto',)

