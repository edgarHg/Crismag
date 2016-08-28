# -*- encoding: utf-8 -*-
from django.contrib.auth.models import *
from django.forms import ModelForm
from factura.apps.admin.models import*
from factura.apps.localidad.models import*
from django import forms
from django.forms import widgets,DecimalField,DateTimeInput,TextInput,CheckboxInput,Select,PasswordInput,DateTimeInput,DateInput,HiddenInput,NullBooleanSelect,RadioSelect,CheckboxInput
from django.utils.safestring import mark_safe

#Formulario para registrar el usuario en la tabla user
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','password')
        widgets = {
            'username': TextInput(attrs={'class':'span12','id':'username', 'placeholder': 'Nombre de usuario','maxlength':'10'}),
            'password': TextInput(attrs={'class':'span12','id':'password', 'placeholder': 'Contrasena','value':'00000'}),
            'first_name': TextInput(attrs={'class':'span12','id':'firstname', 'placeholder': 'Nombre'}),
            'last_name': TextInput(attrs={'class':'span12','id':'lastname','placeholder':'Apellido'}),
            'email': TextInput(attrs={'class':'span12','id':'email','placeholder':'Correo'}),
        }
#Formulario para editar usuario en la tabla user            
class UserFormeditp(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')
        widgets = {
            'first_name': TextInput(attrs={'class':'span12','id':'firstname', 'placeholder': 'Nombre'}),
            'last_name': TextInput(attrs={'class':'span12','id':'lastname','placeholder':'Apellidos'}),
            'email': TextInput(attrs={'class':'span12','id':'email','placeholder':'E-mail'}),
        }
#Formulario para registrar los datos faltantes del usuario en la tabla perfil
class PerfilForm1(forms.ModelForm):
  Estado = forms.ModelChoiceField(queryset=Estados.objects.none(),widget=forms.Select(attrs={'id':'estado','class':'span12'}))
  Localidad = forms.ModelChoiceField(queryset=Municipios.objects.none(),widget=forms.Select(attrs={'id':'id_municipios','class':'span12'}))
  Tipo_usuario = forms.ModelChoiceField(queryset=tipo_usuario.objects.exclude(pk=1),widget=forms.Select(attrs={'id':'Tipo_usuario','class':'span12'}))
  class Meta:
        model = Perfil
        fields = ('Pais','Estado','direccion','codigo_postal','sexo', 'fecha_nacimiento','telefono', 'Localidad','Tipo_usuario')
        widgets = {
            'Pais': Select(attrs={'class':'span12','id':'pais'}),
            'Tipo_usuario': Select(attrs={'class':'span12','id':'Tipo_usuario'}),
            'direccion': TextInput(attrs={'class':'span12','id':'direccion','placeholder':'Direccion'}),
            'codigo_postal': TextInput(attrs={'class':'span12','id':'codigo_postal','placeholder':'86730'}),
            'sexo': Select(attrs={'class':'span12','id':'sexo'}),
            'telefono': TextInput(attrs={'class':'span12','id':'telefono','placeholder':'(993) 231-2013','maxlength':'10'}),
            'Localidad': Select(attrs={'class':'span12','id':'id_municipios'}),
            'Estado':Select(attrs={'class':'span12','id':'estado'}),
            'fecha_nacimiento': DateInput(format=('%m/%d/%Y'),attrs={'name':'fecha','id':'fecha','data-format':'MM/dd/yyyy'}),
        }

        #Formulario para Guardar los datos faltantes del usuario en la tabla perfil
class PerfilFormG(forms.ModelForm):
  class Meta:
    model = Perfil
    fields = ('Pais','Estado','direccion','codigo_postal','sexo','fecha_nacimiento','telefono', 'Localidad','Tipo_usuario')
    widgets = {
            'Pais': Select(attrs={'class':'span12','id':'pais'}),
            'Tipo_usuario': Select(attrs={'class':'span12','id':'Tipo_usuario'}),
            'direccion': TextInput(attrs={'class':'span12','id':'direccion','placeholder':'Direccion'}),
            'codigo_postal': TextInput(attrs={'class':'span12','id':'codigo_postal','placeholder':'86730'}),
            'sexo': Select(attrs={'class':'span12','id':'sexo'}),
            'telefono': TextInput(attrs={'class':'span12','id':'telefono','placeholder':'(993) 231-2013','maxlength':'10'}),
            'Localidad': Select(attrs={'class':'span12','id':'id_municipios'}),
            'Estado':Select(attrs={'class':'span12','id':'estado'}),
            'fecha_nacimiento': DateInput(format=('%m/%d/%Y'),attrs={'name':'fecha','id':'fecha','data-format':'MM/dd/yyyy'}),
        }
        
class PerfilFormeditp(forms.ModelForm):
  def __init__(self, p, *args, **kwargs):
        super(PerfilFormeditp, self).__init__(*args, **kwargs)
        
        municipio = p.Estado.id
        self.fields['Localidad'].queryset = Municipios.objects.filter(estados__id=municipio)
        idTipoUser = p.Tipo_usuario.id
        self.fields['Tipo_usuario'].queryset = tipo_usuario.objects.filter(pk=idTipoUser).exclude(pk=1)
        
  class Meta:
        model = Perfil
        fields = ('Pais','Estado','direccion','codigo_postal','sexo', 'fecha_nacimiento','telefono', 'Localidad','Tipo_usuario')
        widgets = {
            'Pais': Select(attrs={'class':'span12','id':'pais'}),
            'Tipo_usuario': Select(attrs={'class':'span12','id':'Tipo_usuario'}),
            'direccion': TextInput(attrs={'class':'span12','id':'direccion','placeholder':'Direccion'}),
            'codigo_postal': TextInput(attrs={'class':'span12','id':'codigo_postal','placeholder':'86730'}),
            'sexo': Select(attrs={'class':'span12','id':'sexo'}),
            'telefono': TextInput(attrs={'class':'span12','id':'telefono','placeholder':'(993) 231-2013','maxlength':'10'}),
            'Estado':Select(attrs={'class':'span12','id':'estado'}),
            'Localidad': Select(attrs={'class':'span12','id':'id_municipios'}),
            'fecha_nacimiento': DateInput(format=('%m/%d/%Y'),attrs={'name':'fecha','id':'fecha','data-format':'MM/dd/yyyy'}),
        }