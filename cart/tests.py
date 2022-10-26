from django.test import TestCase
from django.urls import reverse

from customers.models import User
from products.models import Category, Product


class TestCartViews(TestCase):
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(email='admin@gmail.com')
        Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                                slug='django-beginners', price='20.00', image='django')
        Product.products.create(category_id=1, title='django intermediate', created_by_id=1,
                                slug='django-intermediate', price='20.00', image='django', is_active=False)
        Product.products.create(category_id=1, title='django advanced', created_by_id=1,
                                slug='django-advanced', price='20.00', image='django', is_active=False)
        self.client.post(reverse('cart_add'), {'productid': 1, 'productqty': 1})
        self.client.post(reverse('cart_add'), {'productid': 2, 'productqty': 3})

    def test_shopping_cart_url(self):
        response = self.client.get(reverse('shopping_cart'))
        self.assertEqual(response.status_code, 200)
    
    def test_cart_add(self):
        response = self.client.post(reverse('cart_add'), {'productid': 3, 'productqty': 1})
        self.assertEqual(response.json(), {'qty': 5})
        response = self.client.post(reverse('cart_add'), {'productid': 2, 'productqty': 1})
        self.assertEqual(response.json(), {'qty': 3})

    def test_cart_delete(self):
        response = self.client.post(reverse('cart_delete'), {'productid': 2})
        self.assertEqual(response.json(), {'qty': 1})

    def test_cart_update(self):
        response = self.client.post(reverse('cart_update'), {'productid': 2, 'action': 'plus'})
        self.assertEqual(response.json(), {'qty': 5})
        response = self.client.post(reverse('cart_update'), {'productid': 2, 'action': 'minus'})
        self.assertEqual(response.json(), {'qty': 3})
