from django.shortcuts import render
from .models import Cart


def cart_view(request):
    cart = Cart.objects.all()
    return render(request, 'cart.html', {'cart':cart})