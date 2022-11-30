from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'store/shop.html')


def pro_detail(request, slug, pk):
    return render(request, 'store/detail.html', {'slug': slug, 'pk': pk})
