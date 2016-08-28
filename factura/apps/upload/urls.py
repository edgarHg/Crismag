from django.conf.urls import patterns, url, include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',

	#documetos
	url(r'^uploaddoc-form/','factura.apps.upload.views.uploaddoc_form'),

	url(r'^upload-archivos/','factura.apps.upload.views.upload_archivos'),

    url(r'^consultar-archivos/','factura.apps.upload.views.consultar_archivos'),

)


