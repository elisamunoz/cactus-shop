from django.conf.urls import url, include
from django.contrib import admin
from .views import about, home
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^products/', include('products.urls')),
    url(r'^about/$', about),
    url(r'^$', home),
    url(r'^accounts/', include('accounts.urls')),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)