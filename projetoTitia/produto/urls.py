from django.urls import path
from .views import lista_produtos  # Importa a view do app produto

urlpatterns = [
    path('', lista_produtos, name='lista_produtos'),  # Define a URL para listar produtos
]