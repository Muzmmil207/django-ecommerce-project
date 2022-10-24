from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_summary, name="cart_summary"),
    path('cart-add', views.cart_add, name="cart_add"),
    path('cart-delete', views.cart_delete, name="cart_delete"),
]
