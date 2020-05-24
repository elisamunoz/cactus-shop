from django.conf.urls import url, include
from django.contrib import admin
from .views import about, home
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
# from products import views as products_list (29)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^about/$', about),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^products/', include('products.urls')),
    url(r'^cart/', include('cart.urls')),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)