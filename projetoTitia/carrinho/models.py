from django.db import models
from cliente.models import Cliente

class Carrinho(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL,null=True,blank=True)
    total = models.PositiveIntegerField(default=0)
    criadoData = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Carro:" + str(self.id)

