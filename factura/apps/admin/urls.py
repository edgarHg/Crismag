from django.conf.urls import patterns, url, include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^administrador/','factura.apps.admin.views.adminis'),
    url(r'^fperso/','factura.apps.admin.views.registrar_personal'),
    url(r'^consultar-personal/','factura.apps.admin.views.consulta_personal'),
    url(r'^ver-personal/(?P<id_personal>\d+)$','factura.apps.admin.views.ver_personal'),
    url(r'^suspender/(?P<id_personal>\d+)$','factura.apps.admin.views.suspender_personal'),
    url(r'^activar/(?P<id_personal>\d+)$','factura.apps.admin.views.activar_personal'),
    url(r'^editar/(?P<id_personal>\d+)$','factura.apps.admin.views.editar_personal'),
    url(r'^capturista/','factura.apps.admin.views.admin_capturista'), #Capturista es lo mismo que personal o empleado. (Solo se coloco para ser mas estetico en la interfa del empleado)
    url(r'^cambiar-contrasena/','factura.apps.admin.views.reset_password'),
   
    
    )


