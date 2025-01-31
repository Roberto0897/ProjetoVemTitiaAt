from django.views.generic import ListView
from .models import Brand

class BrandListView(ListView):
    model = Brand
    template_name = 'marca_list.html'
    context_object_name = 'marca'



