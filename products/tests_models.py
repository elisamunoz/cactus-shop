from django.test import TestCase
from .models import Product


class ProductTests(TestCase):
    """
    Tests the Product model
    """

    def test_str(self):
        test_name = Product(name='product')
        self.assertEqual(str(test_name), 'product')
