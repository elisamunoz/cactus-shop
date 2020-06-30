from django.test import TestCase
from .forms import CreateProduct


class test_CreateProduct(TestCase):
    """
    Tests Create Product Form
    """

    def test_can_create_an_item_with_only_a_name(self):
        form = CreateProduct({'name': 'Create Tests'})
        self.assertFalse(form.is_valid())

    def test_correct_message_for_missing_name(self):
        form = CreateProduct({'name': ''})
        self.assertFalse(form.is_valid())
