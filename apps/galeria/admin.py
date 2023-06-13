from django.contrib import admin

from apps.galeria.models import Cracha

class ListandoCrachas(admin.ModelAdmin):
    list_display = ("id", "nome","cpf" ,"publicada")
    list_display_links = ("id","nome")
    search_fields = ("nome","nome_completo")
    list_filter = ("nome", 'usuario')
    list_editable = ("publicada",)
    list_per_page = 10

admin.site.register(Cracha, ListandoCrachas)
