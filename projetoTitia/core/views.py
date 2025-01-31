from django.shortcuts import render
#from django.views.generic import ListView
from produto.models import Produto


  # def home(request):
   #return render(request, '_home.html')

def home(request):
    produto = Produto.objects.all()
    return render(request, '_home.html', {'produto': produto})

# def get_context_data(self, **kwargs):
#    context = super().get_context_data(**kwargs)
 #   context['produto_list'] =Produto.objects.all()
#    return context
