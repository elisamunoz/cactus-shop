from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import OrderLineItem
from .forms import MakePaymentForm, OrderForm
from products.models import Product
from django.conf import settings
from django.utils import timezone
import stripe


"""
Code taken from Code Institute
"""

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    """  
    This function validates payment, accepting or decling payment
    """
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity
                )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card has been declined")
                return redirect('cart')
            except Exception:
                messages.error(request, "An error ocurred. Payment didn't go through")
                return redirect('cart')

            if customer.paid:
                messages.success(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('products_list'))
            else:
                messages.error(request, "Unable to take payment")
                return redirect('cart')

        else:
            messages.error(
                request, "We were unable to take a payment with that cart")
            return redirect('cart')

    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
