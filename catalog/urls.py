from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductsListView, ProductsDetailView, ProductsTemplateView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, ProductsFilterView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name="home"),
    path('contacts/', ProductsTemplateView.as_view(), name="contacts"),
    path('product_info/<int:pk>/', ProductsDetailView.as_view(), name="product_info"),
    path('product_create/', ProductCreateView.as_view(), name="product_create"),
    path('product_update/<int:pk>', ProductUpdateView.as_view(), name="product_update"),
    path('<int:pk>/product_delete', ProductDeleteView.as_view(), name="product_delete"),
    path('products_filter/<int:category_id>', ProductsFilterView.as_view(), name="products_filter"),
]
