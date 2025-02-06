from django.shortcuts import render

def conta_view(request):
    # Aqui você pega o usuário logado e passa para o template
    return render(request, 'informacoes.html', {'user': request.user})

