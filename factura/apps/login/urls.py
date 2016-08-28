from django.conf.urls import patterns, url, include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','factura.apps.login.views.login'),
    url(r'^validacion-login/$','factura.apps.login.views.validacion_login'),
    url(r'^logout_user/','factura.apps.login.views.cerrar'),

)


