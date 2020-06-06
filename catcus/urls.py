from django.conf.urls import url, include
from django.contrib import admin
from .views import about, home
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from checkout import urls as urls_checkout
from django.views import static
from django.conf import settings
from .settings import MEDIA_ROOT


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^about/$', about),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^products/', include('products.urls')),
    url(r'^cart/', include('cart.urls')),
    url(r'checkout/', include(urls_checkout)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]


# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)