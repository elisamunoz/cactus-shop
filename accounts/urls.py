from django.conf.urls import url
from .import views
from .views import signup_view


app_name ='accounts'

urlpatterns = [
    url(r'^signup/$', signup_view, name="signup")
]