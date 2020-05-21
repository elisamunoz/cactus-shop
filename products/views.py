from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from .forms import CreateProduct


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


@login_required(login_url="accounts/login")
def product_create(request):
    if request.method == 'POST':
        form = CreateProduct(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            form.save()
            return redirect('products_list')
    else:
        form = CreateProduct()
    return render(request, 'productcreate.html', {'form':form})