from django.conf.urls import patterns, url, include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^registro-cliente/','factura.apps.cliente.views.registrar_cliente'),
    url(r'^cliente/','factura.apps.cliente.views.admin_cliente'),
    url(r'^consultar-cliente-general/','factura.apps.cliente.views.consulta_clientes'),
    url(r'^actualizar-cliente/(?P<id_cliente>\d+)/$','factura.apps.cliente.views.actualizar_cliente'),
    url(r'^suspender-cliente/(?P<id_cliente>\d+)/$','factura.apps.cliente.views.suspender_cliente'),
    url(r'^activar-cliente/(?P<id_cliente>\d+)/$','factura.apps.cliente.views.activar_cliente'),
    url(r'^propiedades-cliente/(?P<id_cliente>\d+)/$','factura.apps.cliente.views.propiedades_cliente'),



    #descargar archivo
    url(r'^download-archivos/(?P<name_arc>\w+)/(?P<tipo_arc>\w+)/(?P<id_cliente>\d+)/$','factura.apps.cliente.views.download_archivos'),

    #busqueda de rfc  con ajax
    url( r'^rfc-jax/$','factura.apps.cliente.views.rfsc_ajax'),
    

    

)


