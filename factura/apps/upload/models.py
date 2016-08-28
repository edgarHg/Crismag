# -*- encoding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
import decimal

# Create your models here.

class Archivos(models.Model):
	Archivo = models.FileField(upload_to='documentos', verbose_name='Archivo')

	fecha_registro = models.DateTimeField(auto_now_add=True,null=True, blank=True)
	status = models.BooleanField(default=True)