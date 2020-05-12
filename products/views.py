from django.shortcuts import render
from .models import Product


def products_list(request):
    products = Product.object.all().order_by('?', 'name')
    return render(request, 'products.html', {'products':products})

