from django.views.generic import ListView
from django.shortcuts import render
from produto import views as produto_views
from categoria import views as categoria_views
from django.shortcuts import get_object_or_404
from produto.models import Produto  # Assumindo que Produto está no app 'produto'
from categoria.models import Category  # Assumindo que Categoria está no app 'categoria'
from . import models


class CategoryListView(ListView):
    model = models.Category
    template_name = 'categoria_list.html'
    context_object_name = 'categoria'

    def get_queryset(self):
        categoria_slug = self.kwargs['slug']  # Obtém o slug da URL
        categoria = get_object_or_404(Category, slug=categoria_slug)  # Busca a categoria pelo slug
        return Produto.objects.filter(categoria=categoria)  # Retorna os produtos dessa categoria

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Obtém o contexto base
        categoria_slug = self.kwargs['slug']
        categoria = get_object_or_404(Category, slug=categoria_slug)
        context['titulo_categoria'] = categoria.name  # Passa o nome da categoria
        context['descricao'] = categoria.description  # Passa a descrição da categoria
        return context


# def get_queryset(self):
 #       categoria_slug = self.kwargs['slug']
  #      categoria = categoria_views.objects.get(slug=categoria_slug)
   #     return produto_views.objects.filter(categoria=categoria)

# def get_context_data(self, **kwargs):
 #   context = super().get_context_data(**kwargs)
  #  categoria_slug = self.kwargs['slug']
   # categoria = categoria_views.objects.get(slug=categoria_slug)
   # context['titulo_categoria'] = categoria.nome
   # context['descricao'] = categoria.descricao
    #return context