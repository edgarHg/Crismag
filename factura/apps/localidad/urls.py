from django.conf.urls import patterns, url, include
from django.conf import settings


urlpatterns = patterns('', 
	url( r'^buscar_estados/$', 'factura.apps.localidad.views.vista_buscar_estados'),
    url( r'^buscar_municipios/$', 'factura.apps.localidad.views.vista_buscar_municipios'),

)