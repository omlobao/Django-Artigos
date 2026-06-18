from django.contrib import admin
from .models import Autor, EixoTecnologia


class AutorAadmin(admin.ModelAdmin):
    list_display = ("nome", "biografia", "email",)
    search_fields = ("nome", "biografia", "email",)
    list_filter = ("nome",)


admin.site.register(Autor, AutorAadmin)


class EixoTecnologiaAdmin(admin.ModelAdmin):
    list_display = ("nome", "Autor")
    search_fields = ("nome", "Autor")
    list_filter = ('nome',)

admin.site.register(EixoTecnologia, EixoTecnologiaAdmin)