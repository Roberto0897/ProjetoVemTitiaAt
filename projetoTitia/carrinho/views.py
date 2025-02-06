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
    
    quantidade = int(request.POST.get("quantidade", 1))

    # Cria o item no carrinho
    item, item_created = itensCarrinho.objects.get_or_create(
        carrinho=carrinho, produto=produto,
        defaults={"quantidade": quantidade, "avaliacao": 0, "subtotal": produto.selling_price * quantidade}
    )

    if not item_created:  # Se já existe, apenas aumenta a quantidade
        item.quantidade += quantidade
        item.subtotal = item.quantidade * produto.selling_price
        item.save()

    return redirect('visualizar_carrinho')


from django.contrib.auth.decorators import login_required



@login_required
def excluir_item_carrinho(request, item_id):
    item = get_object_or_404(itensCarrinho, id=item_id, carrinho__cliente=request.user.cliente)
    item.delete()
    return redirect('visualizar_carrinho')

from pedido.models import Pedidos

def finalizar_carrinho(request):
    cliente = request.user.cliente  # Obtém o cliente logado

    carrinho = Carrinho.objects.filter(cliente=cliente).first()
    if not carrinho:
        return HttpResponse("Carrinho não encontrado ou já finalizado.", status=400)

    # Definir os valores para o pedido
    pedido = Pedidos.objects.create(
        carrinho=carrinho,
        ordenado="Pedido Recebido",  # Defina o status inicial do pedido
        enderecoEnvio="Endereço Exemplo",  # Aqui você pode buscar do banco ou pedir ao usuário
        email=request.user.email,
        subTotal=sum(item.subtotal for item in carrinho.itenscarrinho_set.all()),
        desconto=0,  # Pode calcular descontos aqui
        total=sum(item.subtotal for item in carrinho.itenscarrinho_set.all()),  # Total sem desconto
        pedidoStatus="Pedido Recebido",
    )

    # Finalizar o carrinho
    carrinho.itenscarrinho_set.all().delete() # remove itens

    return redirect('pedido_concluido', pedido_id=pedido.id) 