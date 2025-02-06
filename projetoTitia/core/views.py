from django.shortcuts import render ,redirect
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



from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from cliente.models import Cliente


def registrar(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuer = form.save()
            Cliente.objects.create(user=usuer)  # Cria o cliente para o usuário
            login(request, usuer)  # Faz login automático após cadastro
            return redirect('informacoes_conta')  # Redireciona para a página da conta
    else:
        form = UserCreationForm()
    
    return render(request, "registration/registrar.html", {"form": form})

# def get_context_data(self, **kwargs):
#    context = super().get_context_data(**kwargs)
#   context['produto_list'] =Produto.objects.all()
#    return context
