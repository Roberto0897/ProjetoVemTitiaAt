from django.contrib import admin
from . import models


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'description','image',
    'serie_number', 'cost_price', 'selling_price', 'quantity',)
    search_fields = ('name', 'brand', 'category',)
    search_fields = ('nome',)

admin.site.register(models.Produto, ProdutoAdmin)