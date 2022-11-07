from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from products.models import Category, Product

# Create your views here.


def home(request):
    q = request.POST.get('q', '')
    products = Product.products.filter(title__icontains=q)

    context = {'products': products}
    return render(request, 'store/shop.html', context)


def pro_detail(request, slug, pk):
    product = get_object_or_404(Product, slug=slug, id=pk, in_stock=True)
    context = {'product': product}

    return render(request, 'store/detail.html', context)


