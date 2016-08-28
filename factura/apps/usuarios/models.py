# -*- encoding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
import decimal
from factura.apps.localidad.models import*


class Usuarios (models.Model):
	User = models.OneToOneField(User, unique=True, related_name='usuarios')
	
	GENDER_CHOICES = (('M', 'Masculino'),('F', 'Femenino'),)
	sexo = models.CharField(max_length=1, choices=GENDER_CHOICES,null = True, blank=True)
	fecha_nacimiento = models.DateField(blank=True, null=True)
	telefono = models.BigIntegerField(max_length=11,null = True, blank=True)
	Pais = models.ForeignKey(Pais,null = True, blank=True)					
	Estado = models.ForeignKey(Estados,null = True, blank=True)					
	Localidad = models.ForeignKey(Municipios,null = True, blank=True)
	direccion=models.CharField(max_length=200,null = True, blank=True)
	codigo_postal=models.IntegerField(null = True, blank=True)
	
	def __unicode__(self):
		return "%s " % (self.user)