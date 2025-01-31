from django.db import models
from carrinho.models import Carrinho

PEDIDOSTATUS = (
    ("Pedido Recebido ", "Pedido Recebido"),
    ("Pedido Processando ", "Pedido Processando"),
    ("Pedido Caminho ", "Pedido Caminho"),
    ("Pedido Concluido ", "Pedido Concluido"),
    ("Pedido Cancelado ", "Pedido Cancelado"),
)



class Pedidos(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete= models.CASCADE)
    ordenado = models.CharField(max_length=200)
    enderecoEnvio = models.CharField(max_length=200)
    email =models.EmailField(null=True,blank=True)
    subTotal = models.PositiveIntegerField()
    desconto = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    pedidoStatus = models.CharField(max_length= 50 ,choices=PEDIDOSTATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return "Pedido: " + str(self.id)

