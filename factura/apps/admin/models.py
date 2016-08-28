# -*- encoding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
import decimal

from factura.apps.localidad.models import*

# Create your models here.

class tipo_usuario (models.Model):
	nombre = models.CharField('nombre', max_length=50, help_text = 'Escriba el nombre del tipo de usuario', )
	fecha_registro = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.nombre
	
	class Meta:
		ordering = ['nombre'] # como se ordena la consulta
		verbose_name = 'tipo de suario'
		verbose_name_plural = 'tipos de usuaurios'

class Perfil (models.Model):
	User = models.OneToOneField(User, unique=True, related_name='perfil')
	
	GENDER_CHOICES = (('M', 'Masculino'),('F', 'Femenino'),)
	sexo = models.CharField(max_length=1, choices=GENDER_CHOICES)
	fecha_nacimiento = models.DateField(blank=True, null=True)
	telefono = models.BigIntegerField(max_length=11,null = True)

	
	Pais = models.ForeignKey(Pais)					
	Estado = models.ForeignKey(Estados)					
	Localidad = models.ForeignKey(Municipios)
	direccion=models.CharField(max_length=200)
	codigo_postal=models.IntegerField()

	Tipo_usuario = models.ForeignKey(tipo_usuario)

	
	def __unicode__(self):
		return "%s " % (self.user)

	# Revisar modelado extendido