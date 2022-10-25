from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('<slug:uidb64>/<slug:token>/', views.activate, name="activate"),
    path('dashboard/', views.dashboard, name="dashboard"),
]
