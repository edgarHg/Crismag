# -*- encoding: utf-8 -*-
from django.contrib.auth.models import *
from django.forms import ModelForm
from factura.apps.login.models import *
from django import forms
from django.forms import widgets,DecimalField,DateTimeInput,TextInput,CheckboxInput,Select,PasswordInput,DateTimeInput,DateInput,HiddenInput,NullBooleanSelect,RadioSelect,CheckboxInput
from django.utils.safestring import mark_safe


#guardar datos del user
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','password')
        widgets = {
            'username': TextInput(attrs={'class':'span12','id':'username', 'placeholder': 'Nombre de usuario','maxlength':'10'}),
            'password': TextInput(attrs={'class':'span12','id':'password', 'placeholder': 'Contrasena','value':'00000'}),
            'first_name': TextInput(attrs={'class':'span12','id':'firstname', 'placeholder': 'Nombre'}),
            'last_name': TextInput(attrs={'class':'span12','id':'lastname','placeholder':'Apellido'}),
            'email': TextInput(attrs={'class':'span12','id':'email','placeholder':'E-mail'}),
        }
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            u = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('usuario existente')
    
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            u = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Email ya existente')
#fin de guardar datos del user

#actualizar datos del user
class UserFormedit(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': TextInput(attrs={'class':'span12','id':'firstname', 'placeholder': 'Nombre'}),
            'last_name': TextInput(attrs={'class':'span12','id':'lastname','placeholder':'Apellidos'}),
            'email': TextInput(attrs={'class':'span12','id':'email','placeholder':'E-mail'}),
        }
#fin de actualizar dato del user           
        
                    

