from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required


def view_cart(request):
    """ 
    This view allows to see the products in the shopping cart 
    """
    return render(request, 'cart.html')


@login_required
def update_cart(request, id):
    """ 
    This view modify amount of products in the shopping cart 
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('cart'))


@login_required
def add_to_cart(request, id):
    """ 
    This view allows the user to add a certain amount of products
    """
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id] + quantity)
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('home'))