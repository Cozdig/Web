from .models import Product, Category


class ProductService:

    @staticmethod
    def product_filter(category_id):
        products = Product.objects.filter(category=category_id, is_publicate=True)

        return products