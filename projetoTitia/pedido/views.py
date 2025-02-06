from django.shortcuts import render
from .models import Pedidos
from django.http import HttpResponse

def pedido_concluido(request, pedido_id):
    try:
        pedido = Pedidos.objects.get(id=pedido_id)
        return render(request, "pedido_concluido.html", {"pedido": pedido})
    except Pedidos.DoesNotExist:
        return HttpResponse("Pedido não encontrado", status=404)