from django.shortcuts import render
#from django.views.generic import ListView
from produto.models import Produto


  # def home(request):
   #return render(request, '_home.html')

def home(request):
    produto = Produto.objects.all()
    ofertasdasemana = Produto.objects.filter(category__name="ofertasdasemana")
    vibradores = Produto.objects.filter(category__name="vibradores")
    novidadeslacamentos = Produto.objects.filter(category__name="novidadeslacamentos")
    acessorios = Produto.objects.filter(category__name="acessorios")
    Lubrificantes = Produto.objects.filter(category__name="Lubrificantes")

    context = {
      'produto': produto,
      'ofertasdasemana': ofertasdasemana,
      'vibradores': vibradores,
      'novidadeslacamentos': novidadeslacamentos,
      'acessorios': acessorios,
      'Lubrificantes': Lubrificantes,
    }
    return render(request, '_home.html', context)

# def get_context_data(self, **kwargs):
#    context = super().get_context_data(**kwargs)
#   context['produto_list'] =Produto.objects.all()
#    return context
