from django.conf.urls import url, include
from .views import products_list, product_detail


urlpatterns = [
    url(r'^$', products_list, name="products_list"),
    url(r'^(?P<pk>[\w-]+)/$', product_detail, name="product_detail"),
]
