from django.views.generic import ListView
from . import models
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404 
from itensCarrinho.models import itensCarrinho
from carrinho.models import Carrinho
from cliente.models import Cliente
from django.http import HttpResponse


from produto.models import Produto

class CarrinhoListView(ListView):
    model = models.Carrinho
    template_name = 'carrinho_list.html'
    context_object_name = 'carrinho'

def subtotal(self):
        return self.quantidade * self.produto.selling_price


def visualizar_carrinho(request):
    """ Exibe o carrinho do usuário autenticado """
    if not request.user.is_authenticated:
        return HttpResponse("Erro: Usuário não autenticado!", status=400)

    cliente = Cliente.objects.filter(user=request.user).first()
    if not cliente:
        return HttpResponse("Erro: Cliente não encontrado!", status=400)

    carrinho, created = Carrinho.objects.get_or_create(cliente=cliente)
    itens = carrinho.itenscarrinho_set.all()
    total = sum(item.subtotal for item in itens)

    return render(request, "carrinho_list.html", {"itens": itens, "total": total})

def get_carrinho(request):
    """ Obtém ou cria um carrinho para o cliente autenticado """
    if request.user.is_authenticated:
        cliente = Cliente.objects.filter(user=request.user).first()
        if cliente:
            carrinho, created = Carrinho.objects.get_or_create(cliente=cliente)
            return carrinho

    return None  # Retorna None se o usuário não tiver um cliente associado



def adicionar_ao_carrinho(request, produto_id):
    """ Adiciona um produto ao carrinho """
    if not request.user.is_authenticated:
        return HttpResponse("Erro: Usuário não autenticado!", status=400)

    cliente = Cliente.objects.filter(user=request.user).first()
    if not cliente:
        return HttpResponse("Erro: Cliente não encontrado!", status=400)

    produto = get_object_or_404(Produto, id=produto_id)

    # Verifica se o produto tem preço definido
    if produto.selling_price is None:
        return HttpResponse("Erro: O produto não tem preço definido!", status=400)

    # Obtém o carrinho do cliente
    carrinho = get_carrinho(request)
    if not carrinho:
        return HttpResponse("Erro: Carrinho não encontrado!", status=400)

    # Cria o item no carrinho
    itens_carrinho = itensCarrinho.objects.create(
        carrinho=carrinho,
        produto=produto,
        avaliacao=0,  # Valor inicial
        quantidade=1,  # Quantidade inicial
        subtotal=produto.selling_price  # Define subtotal
    )

    return redirect('visualizar_carrinho')


from django.contrib.auth.decorators import login_required

@login_required
def finalizar_compra(request):
    cliente = request.user.cliente
    carrinho = Carrinho.objects.filter(cliente=cliente).first()

    if not carrinho or not carrinho.itenscarrinho_set.exists():
        return redirect('visualizar_carrinho')  # Caso não tenha itens no carrinho
    
    total = sum(item.subtotal for item in carrinho.itenscarrinho_set.all())

    # Cria o pedido
   # pedido = Pedido.objects.create(cliente=cliente, total=total)

    # Adiciona os itens do carrinho ao pedido
   # for item in carrinho.itenscarrinho_set.all():
      #  item.pedido = pedido
      #  item.save()

    # Limpa o carrinho após a compra
    carrinho.itenscarrinho_set.all().delete()

    return render(request, 'pedido_confirmado.html', {})