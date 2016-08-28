# -*- encoding: utf-8 -*-
from django.contrib.auth.models import *
from django.forms import ModelForm
from factura.apps.admin.models import*
from django import forms
from django.forms import widgets,DecimalField,DateTimeInput,TextInput,CheckboxInput,Select,PasswordInput,DateTimeInput,DateInput,HiddenInput,NullBooleanSelect,RadioSelect,CheckboxInput
from django.utils.safestring import mark_safe

from factura.apps.localidad.models import*
from factura.apps.cliente.models import*
    

class PerfilUserviews(forms.ModelForm):
  Estado = forms.ModelChoiceField(queryset=Estados.objects.none(),widget=forms.Select(attrs={'id':'estado','class':'span12'}))
  Localidad = forms.ModelChoiceField(queryset=Municipios.objects.none(),widget=forms.Select(attrs={'id':'id_municipios','class':'span12'}))
  class Meta:
        model = Usuarios
        fields = ('Pais','Estado','Localidad','direccion','codigo_postal','sexo','fecha_nacimiento','telefono')
        widgets = {
            'sexo': Select(attrs={'class':'span12','id':'sexo'}), 
            'fecha_nacimiento': DateInput(format=('%m/%d/%Y'),attrs={'name':'fecha','id':'fecha','data-format':'MM/dd/yyyy'}),
            'telefono': TextInput(attrs={'class':'span12','id':'telefono','placeholder':'(993) 231-2013','maxlength':'10'}),

            'Pais': Select(attrs={'class':'span12','id':'pais'}),
            'Estado':Select(attrs={'class':'span12','id':'estado'}),
            'Localidad': Select(attrs={'class':'span12','id':'localidad'}),
            'direccion': TextInput(attrs={'class':'span12','id':'direccion','placeholder':'Direccion'}),
            'codigo_postal': TextInput(attrs={'class':'span12','id':'codigo_postal','placeholder':'86730'}),
        }

        #Formulario para Guardar los datos faltantes del usuario en la tabla perfil
class PerfilUsersave(forms.ModelForm):
  class Meta:
    model = Usuarios
    fields = ('Pais','Estado','Localidad','direccion','codigo_postal','sexo','fecha_nacimiento','telefono')
    widgets = {
            'sexo': Select(attrs={'class':'span12','id':'sexo'}), 
            'fecha_nacimiento': DateInput(format=('%m/%d/%Y'),attrs={'name':'fecha','id':'fecha','data-format':'MM/dd/yyyy'}),
            'telefono': TextInput(attrs={'class':'span12','id':'telefono','placeholder':'(993) 231-2013','maxlength':'10'}),

            'Pais': Select(attrs={'class':'span12','id':'pais'}),
            'Estado':Select(attrs={'class':'span12','id':'estado'}),
            'Localidad': Select(attrs={'class':'span12','id':'localidad'}),
            'direccion': TextInput(attrs={'class':'span12','id':'direccion','placeholder':'Direccion'}),
            'codigo_postal': TextInput(attrs={'class':'span12','id':'codigo_postal','placeholder':'86730'}),
        }

class PerfilUserEdit(forms.ModelForm):
  def __init__(self, objusuario, *args, **kwargs):
        super(PerfilUserEdit, self).__init__(*args, **kwargs)
        
        if objusuario.Pais_id:
            vvalidar = False
            estado = objusuario.Pais_id
            municipio = objusuario.Estado_id
            print municipio
            self.fields['Estado'].queryset = Estados.objects.filter(pais__id=estado)
            self.fields['Localidad'].queryset = Municipios.objects.filter(estados__id=municipio)
  class Meta:
        model = Usuarios
        fields = ('Pais','Estado','Localidad','direccion','codigo_postal','sexo','fecha_nacimiento','telefono')
        widgets = {
            'sexo': Select(attrs={'class':'span12','id':'sexo'}), 
            'fecha_nacimiento': DateInput(format=('%m/%d/%Y'),attrs={'name':'fecha','id':'fecha','data-format':'MM/dd/yyyy'}),
            'telefono': TextInput(attrs={'class':'span12','id':'telefono','placeholder':'(993) 231-2013','maxlength':'10'}),

            'Pais': Select(attrs={'class':'span12','id':'pais'}),
            'Estado':Select(attrs={'class':'span12','id':'estado'}),
            'Localidad': Select(attrs={'class':'span12','id':'id_municipios'}),
            'direccion': TextInput(attrs={'class':'span12','id':'direccion','placeholder':'Direccion'}),
            'codigo_postal': TextInput(attrs={'class':'span12','id':'codigo_postal','placeholder':'86730'}),
        }
#datos para el cliente empresa/fisica

class ClienteViews(forms.ModelForm):
  Estadoc = forms.ModelChoiceField(queryset=Estados.objects.none(),widget=forms.Select(attrs={'id':'estadoc','class':'span12'}))
  Localidadc = forms.ModelChoiceField(queryset=Municipios.objects.none(),widget=forms.Select(attrs={'id':'id_municipiosc','class':'span12'}))
  class Meta:
        model = Cliente
        fields = ('Nombre_Razons','rfc','telefonoc','Paisc','Estadoc','Localidadc','direccionc','codigo_postalc')
        widgets = {
            'Nombre_Razons': TextInput(attrs={'class':'span12','id':'Nombre_Razons','maxlength':'50'}),
            'rfc': TextInput(attrs={'class':'span12','id':'rfc','maxlength':'20'}),
            'telefonoc': TextInput(attrs={'class':'span12','id':'telefono','placeholder':'(993) 231-2013','maxlength':'10'}),

            'Paisc': Select(attrs={'class':'span12','id':'paisc'}),
            'Estadoc':Select(attrs={'class':'span12','id':'estadoc'}),
            'Localidadc': Select(attrs={'class':'span12','id':'localidadc'}),
            'direccionc': TextInput(attrs={'class':'span12','id':'direccion','placeholder':'Direccion'}),
            'codigo_postalc': TextInput(attrs={'class':'span12','id':'codigo_postal','placeholder':'86730'}),
        }


class ClienteSave(forms.ModelForm):
  class Meta:
    model = Cliente
    fields = ('Nombre_Razons','rfc','telefonoc','Paisc','Estadoc','Localidadc','direccionc','codigo_postalc')
    widgets = {
            'Nombre_Razons': TextInput(attrs={'class':'span12','id':'Nombre_Razons','maxlength':'50'}),
            'rfc': TextInput(attrs={'class':'span12','id':'rfc','maxlength':'20'}),
            'telefonoc': TextInput(attrs={'class':'span12','id':'telefono','placeholder':'(993) 231-2013','maxlength':'10'}),

            'Paisc': Select(attrs={'class':'span12','id':'paisc'}),
            'Estadoc':Select(attrs={'class':'span12','id':'estadoc'}),
            'Localidadc': Select(attrs={'class':'span12','id':'localidadc'}),
            'direccionc': TextInput(attrs={'class':'span12','id':'direccion','placeholder':'Direccion'}),
            'codigo_postalc': TextInput(attrs={'class':'span12','id':'codigo_postal','placeholder':'86730'}),
        }

class ClienteEdit(forms.ModelForm):
  def __init__(self, objcliente, *args, **kwargs):
        super(ClienteEdit, self).__init__(*args, **kwargs)
        
        if objcliente.Paisc_id:
            estado = objcliente.Paisc_id
            municipio = objcliente.Estadoc_id
            self.fields['Estadoc'].queryset = Estados.objects.filter(pais__id=estado)
            self.fields['Localidadc'].queryset = Municipios.objects.filter(estados__id=municipio)
  class Meta:
        model = Cliente
        fields = ('Nombre_Razons','rfc','telefonoc','Paisc','Estadoc','Localidadc','direccionc','codigo_postalc')
        widgets = {
            'Nombre_Razons': TextInput(attrs={'class':'span12','id':'Nombre_Razons','maxlength':'50'}),
            'rfc': TextInput(attrs={'class':'span12','id':'rfc','maxlength':'20'}),
            'telefonoc': TextInput(attrs={'class':'span12','id':'telefono','placeholder':'(993) 231-2013','maxlength':'10'}),

            'Paisc': Select(attrs={'class':'span12','id':'paisc'}),
            'Estadoc':Select(attrs={'class':'span12','id':'estadoc'}),
            'Localidadc': Select(attrs={'class':'span12','id':'id_municipiosc'}),
            'direccionc': TextInput(attrs={'class':'span12','id':'direccion','placeholder':'Direccion'}),
            'codigo_postalc': TextInput(attrs={'class':'span12','id':'codigo_postal','placeholder':'86730'}),
        }


#documentos
class DocFormSave(forms.ModelForm):
    class Meta:
        model = Documentos
        fields = ('pdf','xml',)

 