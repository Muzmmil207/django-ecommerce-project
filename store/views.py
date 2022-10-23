from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product, Category
from django.http import JsonResponse
# Create your views here.


def home(request):
    products = Product.product.all()
    context = {'products': products}

    return render(request, 'store/shop.html', context)


def pro_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    context = {'product': product}

    return render(request, 'store/detail.html', context)


def checkout(request):
    return render(request, 'store/Checkout.html')
