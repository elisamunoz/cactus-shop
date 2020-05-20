from django.conf.urls import url, include
from .views import products_list, product_detail, product_create


urlpatterns = [
    url(r'^$', products_list, name="products_list"),
    url(r'^create/$', product_create, name="create"),
    url(r'^(?P<pk>[\w-]+)/$', product_detail, name="product_detail"),
]
