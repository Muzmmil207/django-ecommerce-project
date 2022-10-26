from django.http.response import JsonResponse
from django.shortcuts import render

from cart.cart import Cart

from .models import Order, OrderItem


def add(request):
    cart = Cart(request)
    if request.method == 'POST':

        order_key = request.POST.get('order_key')
        user = request.user
        carttotal = cart.get_cart_total()

        # Check if order exists
        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            order = Order.objects.create(
                user=user,
                full_name='name',
                address1='add1',
                address2='add2',
                total_paid=carttotal,
                order_key=order_key
            )

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['qty']
                )
 
        return JsonResponse('success', safe=False)
    return JsonResponse('error', safe=False)

