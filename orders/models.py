from django.db import models

from customers.models import User
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='user_order'
    )
    full_name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    post_code = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total_paid = models.DecimalField(max_digits=8, decimal_places=2)
    order_key = models.CharField(max_length=200)
    billing_satus = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.created)

    
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='item_product',
    )
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.product.title)

