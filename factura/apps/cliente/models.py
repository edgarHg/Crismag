# -*- encoding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
import decimal
from factura.apps.usuarios.models import*
from factura.apps.localidad.models import*


class Cliente (models.Model):
	Usuario = models.OneToOneField(Usuarios, unique=True, related_name='usuario')
	Nombre_Razons = models.CharField('nombre', max_length=100, help_text = 'Escriba el nombre o razon social', )
	rfc = models.CharField('rfc', max_length=15, help_text = 'Escriba el rfc', unique=True,)
	telefonoc = models.BigIntegerField(max_length=11,null = True, blank=True)
	
	Paisc = models.ForeignKey(Pais,null=True, blank=True)					
	Estadoc = models.ForeignKey(Estados,null=True, blank=True)					
	Localidadc = models.ForeignKey(Municipios,null=True, blank=True)
	direccionc=models.CharField(max_length=200,null=True, blank=True)
	codigo_postalc=models.IntegerField(null=True, blank=True)
	
	def __unicode__(self):
		return "%s " % (self.user)


class Documentos(models.Model):
	Cliente = models.ForeignKey(Cliente)
	pdf = models.FileField(upload_to='documentos', verbose_name='Archivopdf')
	xml = models.FileField(upload_to='documentos', verbose_name='Archivoxml')

	fecha_registro = models.DateTimeField(auto_now_add=True,null=True, blank=True)
	status = models.BooleanField(default=True)


