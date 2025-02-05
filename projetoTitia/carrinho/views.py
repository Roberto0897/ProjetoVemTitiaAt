from django.views.generic import ListView
from . import models
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from itensCarrinho.models import itensCarrinho
from carrinho.models import Carrinho
from cliente.models import Cliente


from produto.models import Produto

class CarrinhoListView(ListView):
    model = models.Carrinho
    template_name = 'carrinho_list.html'
    context_object_name = 'carrinho'

def subtotal(self):
        return self.quantidade * self.produto.selling_price

def visualizar_carrinho(request):
    cliente = None
    if request.user.is_authenticated:
        cliente = Cliente.objects.filter(user=request.user).first()  # Obtém o cliente

    carrinho, created = Carrinho.objects.get_or_create(cliente=cliente)

    itens = carrinho.itenscarrinho_set.all()  # Busca os itens no carrinho
    total = sum(item.subtotal for item in itens)  # Calcula o total

    return render(request, "carrinho_list.html", {"itens": itens, "total": total})

def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    quantidade = int(request.POST.get("quantidade", 1))

    cliente = None
    if request.user.is_authenticated:
        cliente = Cliente.objects.filter(user=request.user).first()

    carrinho, created = Carrinho.objects.get_or_create(cliente=cliente)

    # Verifica se o item já está no carrinho
    item, item_criado = itensCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)

    if not item_criado:
        item.quantidade += quantidade
    else:
        item.quantidade = quantidade

    item.subtotal = item.quantidade * produto.selling_price  # Atualiza o subtotal
    item.save()

    return redirect("visualizar_carrinho")


def finalizar_compra(request):
    cliente = None
    if request.user.is_authenticated:
        cliente = Cliente.objects.filter(user=request.user).first()

    carrinho = Carrinho.objects.filter(cliente=cliente).first()

    if carrinho:
        carrinho.itenscarrinho_set.all().delete()  # Limpa os itens do carrinho

    return render(request, "carrinho/compra_finalizada.html", {})
