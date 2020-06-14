from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """
    Makes the content of the cart available when rendering every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    cart_total = 0
    product_count = 0
    shipping_cost = 10

    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        cart_total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'id': id,
            'quantity': quantity,
            'product': product,
            'total': quantity * product.price,
        })

    if (cart_total >= 75 ):
        shipping_cost = 0

    return {
        'cart_items': cart_items,
        'product_count': product_count,
        'shipping': shipping_cost,
        'sub_total': cart_total,
        'total': cart_total + shipping_cost,
    }
