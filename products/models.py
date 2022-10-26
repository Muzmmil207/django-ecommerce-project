from django.db import models
from customers.models import User
# Create your models here.


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(max_length=125, db_index=True)
    slug = models.SlugField(max_length=125, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        related_name = 'products',
        on_delete = models.SET_NULL,
        null = True,
        blank = True       
    )
    created_by = models.ForeignKey(
        User,
        related_name = 'product_creater',
        on_delete = models.CASCADE
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='imags/', default='imags/cat-1.jpg')
    slug = models.SlugField(max_length=125)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ['-created']

    def __str__(self):
        return self.title