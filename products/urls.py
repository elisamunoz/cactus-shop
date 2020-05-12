from django.conf.urls import url, include
from .views import products_list


urlpatterns = [
    url(r'^$', products_list),
]
