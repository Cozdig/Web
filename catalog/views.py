from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from catalog.forms import ProductForm
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

class ProductsDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_info.html'
    context_object_name = 'product'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = '/'

    def get_queryset(self):
        user = self.request.user

        if self.request.user.has_perm('catalog.can_unpublish_product'):
            return Product.objects.all()

        return Product.objects.filter(owner=user)

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')

    def get_queryset(self):
        user = self.request.user

        if self.request.user.has_perm('catalog.delete_product'):
            return Product.objects.all()

        return Product.objects.filter(owner=user)