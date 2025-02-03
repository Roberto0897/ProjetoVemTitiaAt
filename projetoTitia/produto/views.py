from django.views.generic import ListView
from . models import Produto
from . import models
from django.shortcuts import render

class ProdutoListView(ListView):
    model = models.Produto
    template_name = 'produto_list.html'
    context_object_name = 'produto'


def lista_produtos(request):
  produto = Produto.objects.all()  # Recupera todos os produtos do banco
  return render(request, 'teste.html', {'produto': produto})