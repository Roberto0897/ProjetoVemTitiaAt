from django.urls import path
from produto.views import lista_produtos


urlpatterns = [
    path('',lista_produtos, name='produto'),
]
