from django.db import models


class Product(models.Model):
    name = models.CharField(max_lengh=100, default='No name')
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='images')



#  name = models.CharField(max_length=254, default='')
#     description = models.TextField()
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     image = models.ImageField(upload_to='images')

#     def __str__(self):
#         return self.name