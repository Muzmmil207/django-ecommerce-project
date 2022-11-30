from django.urls import include, path, re_path

from . import api, views

api_url = [
    path('', api.ProductAPIView.as_view()),
    path('<slug:slug>/<int:pk>/', api.SingleProductAPIView.as_view()),
]

urlpatterns = [
    path('', views.home, name="home"),
    path('<slug:slug>/<int:pk>/', views.pro_detail, name="pro_detail"),
    path('api/', include(api_url)),
]
