from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product
from django.contrib.auth.decorators import login_required


def view_cart(request):
    """ 
    This view allows to see the products in the shopping cart 
    """
    return render(request, 'cart.html')


@login_required
def update_cart(request):
    """ 
    This view modify amount of products in the shopping cart 
    """
    try:
        cart = request.session.get('cart', {})

        for key, value in request.POST.items():
            itemId = str(key)

            if itemId in cart:
                quantity = int(value)

                if quantity > 0:
                    cart[itemId] = quantity
                else:
                    cart.pop(itemId)

        request.session['cart'] = cart
        return redirect(reverse('cart'))

    except Exception:
        return redirect('404')


@login_required
def add_to_cart(request, id):
    """ 
    This view allows the user to add a certain amount of products
    """
    try:
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})
        product = get_object_or_404(Product, pk=id)

        if id in cart:
            cart[id] = int(cart[id] + quantity)
        else:
            cart[id] = cart.get(id, quantity)

        request.session['cart'] = cart
        messages.success(request, "You added " +
                         product.name + " to your cart")
        return redirect(reverse('products_list'))

    except Exception:
        return redirect('404')
