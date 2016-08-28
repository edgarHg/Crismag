from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'factura.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #apps
    url(r'^',include('factura.apps.login.urls')),
    url(r'^',include('factura.apps.localidad.urls')),
    url(r'^',include('factura.apps.admin.urls')),

    url(r'^',include('factura.apps.usuarios.urls')),
    url(r'^',include('factura.apps.cliente.urls')),

    url(r'^',include('factura.apps.upload.urls')),

    url(r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT,}
    ),
)
