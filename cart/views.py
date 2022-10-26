from django.http import JsonResponse
from django.shortcuts import render
from products.models import Product

from .cart import Cart

# Create your views here.


def shopping_cart(request):
    return render(request, 'cart/summary.html')


def cart_add(request):
    cart = Cart(request)
    if request.method == 'POST':
        product_id = request.POST.get('productid')
        product_qty = int(request.POST.get('productqty'))
        product = Product.objects.get(id=product_id)
        cart.add(product=product, qty=product_qty)


    response = JsonResponse(f'{product.titel} add to the cart', safe=False)
    return response
        

def cart_update(request):
    cart = Cart(request)
    if request.method == 'POST':
        product_id = request.POST.get('productid')
        action = request.POST.get('action')
        cart.update(product_id=product_id, action=action)

    response = JsonResponse('cart updated', safe=False)
    return response


def cart_delete(request):
    cart = Cart(request)
    if request.method == 'POST':
        product_id = request.POST.get('productid')
        cart.delete(product_id=product_id)

    response = JsonResponse('cart updated', safe=False)
    return response
