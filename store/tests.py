from importlib import import_module

from customers.models import User
from django.conf import settings
from django.http import HttpRequest
from django.test import Client, TestCase
from django.urls import reverse
from products.models import Category, Product

from .views import home


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        User.objects.create(email='admin@gmail.com')
        Category.objects.create(name='django', slug='django')
        self.object1 =  Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                                                slug='django-beginners', price='20.00', image='django')

    def test_homepage_url(self):
        """
        Test homepage response status
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test items response status
        """
        data = self.object1
        response = self.c.get(reverse('pro_detail', args=[data.slug, data.id]))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        """
        Example: code validation, search HTML for text
        """
        request = HttpRequest()
        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore()
        response = home(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>EShopper</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
