from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('product-details/<slug:slug>/', views.pro_detail, name="pro_detail"),
]
