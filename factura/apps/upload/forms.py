# -*- encoding: utf-8 -*-
from django.contrib.auth.models import *
from django.forms import ModelForm
from factura.apps.admin.models import*
from django import forms
from django.forms import widgets,DecimalField,DateTimeInput,TextInput,CheckboxInput,Select,PasswordInput,DateTimeInput,DateInput,HiddenInput,NullBooleanSelect,RadioSelect,CheckboxInput
from django.utils.safestring import mark_safe
from factura.apps.upload.models import* #bueno


#documentos
class ArFormSave(forms.ModelForm):
    class Meta:
        model = Archivos
        fields = ('Archivo',)

 