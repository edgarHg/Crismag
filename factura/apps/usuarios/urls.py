from django.conf.urls import patterns, url, include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^usuarios/','factura.apps.usuarios.views.usuarios'),
    url(r'^registro-cliente/','factura.apps.cliente.views.registrar_cliente'),
   #url(r'^consultar-personal/','factura.apps.admin.views.consulta_personal'),
    #url(r'^suspender/','factura.apps.admin.views.suspender_personal'),
    #url(r'^activar/','factura.apps.admin.views.activar_personal'),

)


