from django.contrib import admin
from . import models


class PedidoAdmin(admin.ModelAdmin):
    list_display = ('carrinho', 'enderecoEnvio', 'email', 'subTotal', 'desconto', 'total' , 'pedidoStatus')
    search_fields = ('carrinho',)

admin.site.register(models.Pedidos, PedidoAdmin)
