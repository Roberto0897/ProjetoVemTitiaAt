from django.contrib import admin
from . import models

class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'total',)
    search_fields = ('cliente',)

admin.site.register(models.Carrinho, CarrinhoAdmin)