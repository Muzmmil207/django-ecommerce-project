import stripe

from django.shortcuts import render
from django.conf import settings

from cart.cart import Cart


def checkout(request):

    cart = Cart(request)
    total = str(cart.get_cart_total())
    total = total.replace('.', '')
    total = int(total)

    stripe.api_key = 'sk_test_51Lx39zGJRosc7bVBIU2bOfWpBti3TDHtnjNp6kDaZRGPFVa2Seq9LnfD9FUW7BDgdoujYr63f5ZeaemIbuqQYPNs00ddSQBBuj'
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbp',
        metadata={'userid': request.user.id}
    )

    return render(request, 'payment/home.html', {'client_secret': intent.client_secret})
