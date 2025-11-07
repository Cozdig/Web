from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def home_page(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'home.html', context=context)

def contacts_page(request):
    return render(request, 'contacts.html')

def product_info_page(request, product_id):
    product = Product.objects.get(pk=product_id)
    context = {
        'name' : product.name,
        'description' : product.description,
        'image' : product.image,
        'category': product.category,
        'price' : product.price,
        'create_date': product.created_at,
        'update_date': product.updated_at
    }
    return render(request, 'product_info.html', context=context)