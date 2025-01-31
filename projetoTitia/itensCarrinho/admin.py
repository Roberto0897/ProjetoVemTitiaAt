from django.contrib import admin
from . import models

class itensCarrinhoAdmin(admin.ModelAdmin):
    list_display = ('carrinho', 'produto', 'avaliacao', 'quantidade', 'subtotal',)
    search_fields = ('carrinho',)

admin.site.register(models.itensCarrinho, itensCarrinhoAdmin)
