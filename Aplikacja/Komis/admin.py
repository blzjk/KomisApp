from django.contrib import admin
from django.utils.html import format_html
from .models import Kolor, Marka, Zdjecie, Samochod


@admin.register(Samochod)
class SamochodAdmin(admin.ModelAdmin):
    list_display = ['marka', 'model', 'data_produkcji', 'kolor', 'czyWidoczny']
    list_filter = ['czyWidoczny', 'marka', 'rezerwacja', 'paliwo', 'rodzaj']

    def show_url(self, obj):
        if obj.source is not None:
            return format_html(f'<a href="{obj.source}" target="_blank">{obj.source}</a>')
        else:
            return ''

    show_url.short_description = 'url'


@admin.register(Marka)
class MarkaAdmin(admin.ModelAdmin):
    search_fields = ['nazwa']
    list_display = ['nazwa']
    list_filter = ['nazwa']


@admin.register(Kolor)
class KolorAdmin(admin.ModelAdmin):
    search_fields = ['nazwa']
    list_display = ['nazwa']
    list_filter = ['nazwa']


@admin.register(Zdjecie)
class Zdjecie(admin.ModelAdmin):
    list_display = ['foto']


class ImageInline(admin.TabularInline):
    model = Zdjecie


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]




