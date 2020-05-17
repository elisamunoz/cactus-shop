from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import HttpResponse


def products_list(request):
    """ Creates a view that returns a products lists
    """
    products = Product.object.all().order_by('?', 'name')
    return render(request, 'products.html', {'products':products})

def product_detail(request, pk):
    """ Creates a view that returns a single Products based on its ID or returns a 404 error if product doesn't exist
    """
    product = get_object_or_404(Product, pk=pk )
    product.save()
    return render(request, "productdetail.html", {'product':product})