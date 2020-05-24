from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Cart
from products.models import Product

def view_cart(request):

    """ This views allows to see the products in the shopping cart """
    cart = Cart.objects.all()
    return render(request, 'cart.html', {'cart':cart})


@login_required
def update_cart(request, id):
    """ This views modify amount of products in the shopping cart """
    cart = Cart.objects.all()
    try:
        print('cart')
        print(cart.products)
        product = Product.object.get(id=id)
        a = cart.products.all()
        print('ddd')
        print(a)
        if not product in cart.products.all():
            print('hi')
            #adds to the many to many field
            cart.products.add(product)  
        else:
            print('no')
            cart.products.remove(product)
    except Product.DoesNotExist:
        pass
    except:
        pass
    # if not product in cart.products.all():
    #     #adds to the many to many field
    #     cart.products.add(product)  
    # else:
    #     cart.products.remove(product)

    return HttpResponseRedirect(reverse("cart"))
    