
from django.contrib import admin
from django.urls import path ,include
from marca import views as marca_views
from produto import views as produto_views
from categoria import views as categoria_views
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('marca/list/', marca_views.BrandListView.as_view(), name='brand_list'),
    path('produto/list/', produto_views.ProdutoListView.as_view(), name='produto_list'),
   # path('acessorios/', categoria_views.CategoryListView.as_view(), name='category_list'),
    path('categoria/<slug:slug>/', categoria_views.CategoryListView.as_view(), name='category_list'),
    path('produto/', include('produto.urls')),
    
   # path('produtos/', include('produto.urls')), 

     
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#if settings.DEBUG:
  #  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)