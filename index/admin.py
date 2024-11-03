from django.contrib import admin
from index.models import Texto

class ListandoTextos(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'sub_titulo', 'data_postagem', 'visivel')
    list_display_links =('id', 'titulo')
    search_fields = ('titulo', )
    list_per_page = 10
    list_editable = ('visivel',)

admin.site.register(Texto, ListandoTextos)
