from django.shortcuts import render, redirect
from products.models import Product, Category
from django.http import JsonResponse
# Create your views here.



def home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/home.html')

