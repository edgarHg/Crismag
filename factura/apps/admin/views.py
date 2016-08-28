# -*- encoding: utf-8 -*-
# importamos para la autentificacion en django
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

from django.contrib.auth.models import User, Group, Permission
# importamos para la autentificacion en django

from django.core.urlresolvers import reverse

from django.core.exceptions import PermissionDenied
from django.contrib import messages
#importamos para las url html
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.template.response import *
from django.shortcuts import render_to_response, get_object_or_404,render
#importamos para las url html

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core import serializers

from django.core.exceptions import ObjectDoesNotExist

from django.core.mail import send_mail, BadHeaderError




import json
from django.db.models import Q

import datetime 
import calendar
import time
from datetime import date, timedelta


from reportlab.pdfgen import canvas

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter, landscape, A4
from reportlab.lib.units import cm, mm, inch, pica
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_LEFT, TA_CENTER
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate,PageTemplate, Paragraph, Spacer, Image
from reportlab.lib import colors

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate,PageTemplate, Paragraph, Spacer, Image
from reportlab.lib.pagesizes import letter, landscape, A4, portrait
from reportlab.lib.units import cm, mm, inch, pica
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_LEFT, TA_CENTER
from reportlab.lib import colors

import os


from reportlab.rl_config import defaultPageSize
import locale
PAGE_HEIGHT=defaultPageSize[1]; PAGE_WIDTH=defaultPageSize[0]

Title = ''
pageinfo = ""


from  reportlab.platypus import PageBreak
from django.core.paginator import Paginator, InvalidPage, EmptyPage
import xlwt
from xlwt import *

from factura.apps.login.models import* #bueno
from factura.apps.login.forms import*
from factura.apps.admin.forms import*
from factura.apps.localidad.models import*
from factura.apps.cliente.models import*
from factura.apps.upload.models import* #bueno

def validator(user):
  if user.is_authenticated():
    iduser=user.is_staff
    if iduser:
      estatus=True
      return estatus

@user_passes_test(validator,login_url="/")
@login_required(login_url='/')
def adminis(request):
  objclientes=Cliente.objects.filter(Usuario__User__is_active=True)
  a = True
  ctx={'activoa':a,
       'clientes':objclientes}
  return render_to_response('administracion.html',ctx, context_instance=RequestContext(request))

@user_passes_test(validator,login_url="/")
def registrar_personal(request):
    if request.method == 'POST':
        userForm=UserForm(request.POST) 
        perfilForm=PerfilFormG(request.POST)
        if userForm.is_valid() and perfilForm.is_valid():
	    
            username = userForm.cleaned_data['username']
            password = userForm.cleaned_data['password']
            first_name = userForm.cleaned_data['first_name']
            last_name = userForm.cleaned_data['last_name']
            email = userForm.cleaned_data['email']
            
            sexo = perfilForm.cleaned_data['sexo']
            fecha_nacimiento = perfilForm.cleaned_data['fecha_nacimiento']
            telefono = perfilForm.cleaned_data['telefono']

            objpais = perfilForm.cleaned_data['Pais']
            objestado = perfilForm.cleaned_data['Estado']
            objlocalidad = perfilForm.cleaned_data['Localidad']
            objdireccion = perfilForm.cleaned_data['direccion']
            objcodigo_postal = perfilForm.cleaned_data['codigo_postal']

            usuariof = perfilForm.cleaned_data['Tipo_usuario']

            create_user = User.objects.create_user(username= username, email= email, password=password)
            
            create_user.first_name = first_name
            create_user.last_name = last_name

            user_id=create_user.save()
            user_id=create_user.id
            user_id=User.objects.get(pk=user_id)

            userf = Perfil()

            userf.sexo=sexo
            userf.fecha_nacimiento=fecha_nacimiento
            userf.telefono=telefono

            userf.Pais=objpais
            userf.Estado=objestado
            userf.Localidad=objlocalidad
            userf.direccion=objdireccion
            userf.codigo_postal=objcodigo_postal

            userf.Tipo_usuario=usuariof
            userf.User = user_id

            userf.save()

            msj='Los datos se guardaron correctamente.' 
            messages.add_message(request, messages.SUCCESS, msj)
            return HttpResponseRedirect('/consultar-personal/')
        else:
            msj='Error '
            messages.add_message(request, messages.ERROR, msj)
            return HttpResponseRedirect('/fperso/')     
    else:
        userForm=UserForm()  
        perfilForm=PerfilForm1()
        a=True
        ctx={'p':perfilForm,'u':userForm,'activop':a}      
        return render_to_response( 'fpersonal.html', ctx, context_instance = RequestContext(request))

@user_passes_test(validator,login_url="/")     
def consulta_personal(request):
  personal=Perfil.objects.filter(User__is_active=True)
  a=True
  ctx={'perfil':personal,'activop':a}
  return render_to_response('consulta_personal.html',ctx, context_instance=RequestContext(request))
  
@user_passes_test(validator,login_url="/")   
def suspender_personal(request,id_personal):
  u = User.objects.get(pk=id_personal)
  u=User.objects.filter(pk=id_personal).update(is_active=False)
  personal=Perfil.objects.all()
  a=True
  ctx={'perfil':personal,'activop':a}
  return render_to_response('consulta_personal.html',ctx, context_instance=RequestContext(request))

@user_passes_test(validator,login_url="/")  
def activar_personal(request,id_personal):
  u = User.objects.get(pk=id_personal)
  u = User.objects.filter(pk=id_personal).update(is_active=True)
  personal=Perfil.objects.all()
  a=True
  ctx={'perfil':personal,'activop':a}
  return render_to_response('consulta_personal.html',ctx, context_instance=RequestContext(request))
  
@user_passes_test(validator,login_url="/")
def ver_personal(request,id_personal):
    u = User.objects.get(pk=id_personal)
    personal=Perfil.objects.get(User__id=id_personal)

    a=True
    ctx={'activop':a,'perfil':personal,'u':u}
    return render_to_response('ver_personal .html',ctx, context_instance=RequestContext(request))

@user_passes_test(validator,login_url="/")
def editar_personal(request,id_personal):
    u = User.objects.get(pk=id_personal)
    p = Perfil.objects.get(User__id=id_personal)
    userForm=UserFormeditp(instance=u)  
    perfilForm=PerfilFormeditp(p,instance=p)

    if request.method == 'POST':
        userForm=UserFormeditp(request.POST, instance=u)  
        perfilForm=PerfilFormG(request.POST, instance=p)

        if perfilForm.is_valid() and userForm.is_valid():
            # formulario validado correctamente
            userForm.save()
            perfilForm.save()

            userForm=UserFormeditp(request.POST,instance=u)  
            perfilForm=PerfilFormG(request.POST,instance=p)

            msj='Los datos se actualizaron correctamente.' 
            messages.add_message(request, messages.SUCCESS, msj)
            a=True
            ctx={'p':perfilForm,'u':userForm,'activop':a}
            return HttpResponseRedirect("/ver-personal/"+id_personal)
        else:
            msj='Favor de Corregir los siguientes errores.'
            messages.add_message(request, messages.ERROR, msj)
            a=True
            ctx={'p':perfilForm,'u':userForm,'activop':a,'vedit':a}
            return render_to_response('fpersonal.html',ctx, context_instance=RequestContext(request))

    else:
        a=True  
        ctx={
        'p':perfilForm,
        'u':userForm,
        'activop':a,
        'edit':a
        }
        return render_to_response('fpersonal.html',ctx, context_instance=RequestContext(request))

@login_required(login_url="/")
def admin_capturista(request):
  objclientes=Cliente.objects.filter(Usuario__User__is_active=True)
  a=True
  ctx={
  'clientes':objclientes,
  'activoc':a,
  }
  a=True
  ctx={
    'activoc':a,
    'clientes':objclientes,}
  return render_to_response('capturista.html',ctx, context_instance=RequestContext(request))
  

@login_required(login_url="/")
def reset_password(request):
    if request.method=='POST':
        user=request.POST['user']
        nuevo=request.POST['nuevo']
        try:
            usuario = User.objects.get(username__exact=user,is_active=True)
            if request.user.username == usuario.username:
                usuario.set_password(nuevo)
                usuario.save()
                msj='Contraseña cambiada correctamente.' 
                messages.add_message(request, messages.SUCCESS, msj)
                return HttpResponseRedirect('/cambiar-contrasena/')
            else:
                msj='No es tu nombre de usuario.' 
                messages.add_message(request, messages.ERROR, msj)
                return HttpResponseRedirect('/cambiar-contrasena/')    
        except User.DoesNotExist:
            msj='Este nombre de usuario no existe en la base de datos.' 
            messages.add_message(request, messages.ERROR, msj)
            return HttpResponseRedirect('/cambiar-contrasena/')     
    else:
        objarchivos=Archivos.objects.filter(status=True).order_by('-id')[:1] 
        a=True
	ctx={
	  'adminclint':a,
      'activocclit':a,
      'objarchivos':objarchivos,
	  }
        return render_to_response('cambiar_password.html', ctx,context_instance=RequestContext(request))