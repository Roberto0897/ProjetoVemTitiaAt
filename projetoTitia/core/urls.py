
from django.contrib import admin
from django.urls import path ,include
from marca import views as marca_views
from produto import views as produto_views
from categoria import views as categoria_views
from carrinho import views as carrinho_views
from cliente import views as cliente_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import registrar




urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/', registrar, name="registrar"),

    path('marca/list/', marca_views.BrandListView.as_view(), name='brand_list'),
    #path('produto/list/', produto_views.ProdutoListView.as_view(), name='produto_list'),
    path('categoria/acessorios/', categoria_views.AcessoriosListView.as_view(), name='acessorios_list'),
    path('categoria/cosmeticosintimos/', categoria_views.CosmeticosListView.as_view(), name='cosmeticos_list'),
    path('categoria/estiloeconforto/', categoria_views.EstiloListView.as_view(), name='estilo_list'),
    path('categoria/cuidadospessoais/', categoria_views.CuidadosListView.as_view(), name='cuidados_list'),
    path('categoria/bemestarfeminino/', categoria_views.FemininaListView.as_view(), name='feminina_list'),
    path('categoria/bemestarmasculino/', categoria_views.MasculinoListView.as_view(), name='masculino_list'),
    path('categoria/ofertasdasemana/', categoria_views.OfertaListView.as_view(), name='oferta_list'),
    path('categoria/novidadeselacamentos/', categoria_views.NovidadesListView.as_view(), name='novidade_list'),
    path('produto/list/', produto_views.lista_produtos, name='produto_list'),
    path('produto/<int:pk>/', produto_views.detalhe_produto, name='produto_detalhe'),
    path('carrinho/', carrinho_views.visualizar_carrinho, name='visualizar_carrinho' ),
    path('adicionar/<int:produto_id>/', carrinho_views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('finalizar/', carrinho_views.finalizar_compra, name="finalizar_compra"),
    #path('conta/', views.conta_view, name='informacoes_conta'),
    path('conta/', cliente_views.conta_view, name='informacoes_conta'),
  



    
   # path('categoria/<slug:slug>/', categoria_views.CategoryListView.as_view(), name='category_list'),
    path('produto/', include('produto.urls')),
    
   # path('produtos/', include('produto.urls')), 

     
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#if settings.DEBUG:
  #  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)