from django.test import TestCase
from .models import Product

class TestViews(TestCase):
    def test_get_products_page(self):
        page = self.client.get("/products/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")


       