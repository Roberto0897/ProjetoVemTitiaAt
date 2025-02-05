from django.db import models
from carrinho.models import Carrinho
from produto.models import Produto

class itensCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    avaliacao = models.PositiveIntegerField()
    quantidade = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

    def __str__(self):
        return "Carro:" + str(self.carrinho.id) + "itensCarrinho:" + str(self.id)