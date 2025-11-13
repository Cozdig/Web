from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductsListView, ProductsDetailView, ProductsTemplateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name="home"),
    path('contacts/', ProductsTemplateView.as_view(), name="contacts"),
    path('product_info/<int:pk>/', ProductsDetailView.as_view(), name="product_info"),
]
