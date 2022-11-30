from products.models import Category, Product
from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response

from .serializers import ProductSerializer


class ProductAPIView(generics.GenericAPIView, mixins.ListModelMixin):
    """
    API endpoint that returns all products
    """
    queryset = Product.active.all()
    serializer_class=ProductSerializer

    def get(self, request):
        return self.list(request)


class SingleProductAPIView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
):
    """
    API endpoint that returns single product
    """

    queryset =  Product.active.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    # def retrieve(self, request, slug=None, pk=None):
    #     queryset = Product.objects.filter(slug=slug, id=pk)
    #     serializer = ProductSerializer(queryset, many=False)
    #     return Response(serializer.data)
