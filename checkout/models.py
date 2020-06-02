from django.db import models
from products.models import Product

class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    email_address = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=12, blank=False)
    address = models.CharField(max_length=50, blank=False)
    city_town = models.CharField(max_length=50, blank=False)
    country = models.CharField(max_length= 40, blank=False)
    postcode = models.CharField(max_length= 10, blank=True)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.product.name, self.quantity, self.product.price)