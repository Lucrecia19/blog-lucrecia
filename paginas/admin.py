from django.contrib import admin
from .models import Page 

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'fecha_publicacion')
    search_fields = ('titulo', 'subtitulo')