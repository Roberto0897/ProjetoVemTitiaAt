from django.views.generic import ListView
from . models import Produto
from . import models
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

class ProdutoListView(ListView):
    model = models.Produto
    template_name = 'produto_list.html'
    context_object_name = 'produto'


# def lista_produtos(request):
 # produto = Produto.objects.all()  # Recupera todos os produtos do banco
 # return render(request, 'teste.html', {'produto': produto})
def lista_produtos(request):
    query = request.GET.get('q' , '').strip()   # Obtém o termo pesquisado
 

    if query:
        produto = Produto.objects.filter(name__icontains=query)  # Filtra pelo nome do produto
    else:
        produto = Produto.objects.all()  # Mostra todos os produtos
      
    return render(request, 'produto_list.html', {'produto': produto, 'query': query})



def detalhe_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, '_produtoDetalhe.html', {'produto': produto})

# def adicionar_ao_carrinho(request, produto_id):
  #  produto = get_object_or_404(Produto, id=produto_id)
#    quantidade = int(request.POST.get('quantidade', 1))