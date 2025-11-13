from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from catalog.models import Product


# Create your views here.
class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

class ProductsTemplateView(TemplateView):
    model = Product
    template_name = 'catalog/contacts.html'
    context_object_name = 'product'

class ProductsDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_info.html'
    context_object_name = 'product'

