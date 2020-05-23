from django.db import models
from products.models import Product

class Cart(models.Model):
    products = models.ManyToManyField(Product, null=True, blank=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, default= 0.0)

    def __unicode__(self):
        return "cart id: %s" %(self.id)