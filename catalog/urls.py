from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home_page, contacts_page, product_info_page

app_name = CatalogConfig.name

urlpatterns = [
    path('', home_page, name="home"),
    path('contacts/', contacts_page, name="contacts"),
    path('product_info/<int:product_id>/', product_info_page, name="product_info"),
]
