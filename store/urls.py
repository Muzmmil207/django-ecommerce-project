from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<slug:slug>/<int:pk>/', views.pro_detail, name="pro_detail"),
    path('checkout/', views.checkout, name="checkout"),
]
