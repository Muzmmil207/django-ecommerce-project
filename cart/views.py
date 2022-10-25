from django.shortcuts import render
from django.http import JsonResponse

from .cart import Cart
from products.models import Product
# Create your views here.


def cart_summary(request):
    return render(request, 'cart/summary.html')


def cart_add(request):
    cart = Cart(request)
    if request.method == 'POST':
        print(request.POST)
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = Product.objects.get(id=product_id)
        cart.add(product=product, qty=product_qty)

    cartqty = cart.__len__()
    response = JsonResponse({'qty': cartqty})
    
    return response
        

def cart_update(request):
    cart = Cart(request)
    if request.method == 'POST':
        # print(request.POST)
        product_id = request.POST.get('productid')
        action = request.POST.get('action')
        cart.update(product_id=product_id, action=action)

    cartqty = cart.__len__()
    response = JsonResponse({'qty': cartqty})
    
    return response


def cart_delete(request):
    cart = Cart(request)
    if request.method == 'POST':
        product_id = request.POST.get('productid')
        cart.delete(product_id=product_id)

    cartqty = cart.__len__()
    response = JsonResponse({'qty': cartqty})
    
    return response
