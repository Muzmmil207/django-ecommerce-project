from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('products/', include('products.urls')),
    path('customer/', include('customers.urls')),    
    path('cart/', include('cart.urls')),    
    path('payment/', include('payment.urls')),
    path('order/', include('orders.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
