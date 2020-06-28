from django.conf.urls import url
from .views import signup_view, signin_view, logout_view, profile_view


app_name ='accounts'

urlpatterns = [
    url(r'^signup/$', signup_view, name="signup"),
    url(r'^profile/$', profile_view, name='profile'),
    url(r'^login/$', signin_view, name="signin"),
    url(r'^logout/$', logout_view, name="logout")
]