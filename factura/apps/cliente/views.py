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

from factura.apps.login.models import* #bueno
from factura.apps.login.forms import*
from factura.apps.cliente.forms import*
from factura.apps.localidad.models import*
from factura.apps.upload.models import* #bueno

import urllib
from django.core.files import File

import datetime 
import calendar
import time
from datetime import date, timedelta

def validatoradmin(user):
  if user.is_authenticated():
    iduser=user.is_staff
    iduser2=user.id
    if iduser == True:
      estatus=True
      return estatus
    else:
        objcap=Perfil.objects.get(User__id=iduser2)
        vtipo=objcap.Tipo_usuario_id
        if vtipo == 2:
            estatus=True
            return estatus  

     



@user_passes_test(validatoradmin,login_url="/")
def registrar_cliente(request):
    if request.method == 'POST':
        userForm=UserForm(request.POST) 
        perfilForm=PerfilUsersave(request.POST)
        ClienteSaveForm = ClienteSave(request.POST)
        if userForm.is_valid() and perfilForm.is_valid() and ClienteSaveForm.is_valid():
	    
            username = userForm.cleaned_data['username']
            password = userForm.cleaned_data['password']
            first_name = userForm.cleaned_data['first_name']
            last_name = userForm.cleaned_data['last_name']
            email = userForm.cleaned_data['email']
            
            #datos del usuario
            sexo = perfilForm.cleaned_data['sexo']
            fecha_nacimiento = perfilForm.cleaned_data['fecha_nacimiento']
            telefono = perfilForm.cleaned_data['telefono']

            objpais = perfilForm.cleaned_data['Pais']
            objestado = perfilForm.cleaned_data['Estado']
            objlocalidad = perfilForm.cleaned_data['Localidad']
            objdireccion = perfilForm.cleaned_data['direccion']
            objcodigo_postal = perfilForm.cleaned_data['codigo_postal']
            #fin de dasros del usuario


            #datos del cliente
            Nombre_Razonsc = ClienteSaveForm.cleaned_data['Nombre_Razons']
            rfcc = ClienteSaveForm.cleaned_data['rfc']
            telefonoc = ClienteSaveForm.cleaned_data['telefonoc']

            objpaisc = ClienteSaveForm.cleaned_data['Paisc']
            objestadoc = ClienteSaveForm.cleaned_data['Estadoc']
            objlocalidadc = ClienteSaveForm.cleaned_data['Localidadc']
            objdireccionc = ClienteSaveForm.cleaned_data['direccionc']
            objcodigo_postalc = ClienteSaveForm.cleaned_data['codigo_postalc']
            #fin de datos del cliente

            create_user = User.objects.create_user(username= username, email= email, password=password)
            
            create_user.first_name = first_name
            create_user.last_name = last_name

            user_id=create_user.save()#guardamos el user
            user_id=create_user.id
            user_id=User.objects.get(pk=user_id)

            userf = Usuarios()

            userf.sexo=sexo
            userf.fecha_nacimiento=fecha_nacimiento
            userf.telefono=telefono

            userf.Pais=objpais
            userf.Estado=objestado
            userf.Localidad=objlocalidad
            userf.direccion=objdireccion
            userf.codigo_postal=objcodigo_postal

            userf.User = user_id

            userf.save()#guardamos el usuario y recuperamos su id
            viduser =Usuarios.objects.get(User__id=user_id.id)#consultamos el id del usuario para guardarlo


            #datos del cliente
            objcliente = Cliente()
            objcliente.Usuario =viduser
            objcliente.Nombre_Razons =Nombre_Razonsc
            objcliente.rfc =rfcc
            objcliente.telefonoc =telefonoc

            objcliente.Paisc=objpaisc
            objcliente.Estadoc=objestadoc
            objcliente.Localidadc=objlocalidadc
            objcliente.direccionc=objdireccionc
            objcliente.codigo_postalc=objcodigo_postalc
            objcliente.save()#guardamos el cliente
            #fin de datos del cliente

            ficheros = "C:/proyectos/factura/factura/archivos/documentos/"+str(rfcc)#insertamos el rfc para crear al directorio
            if not os.path.exists(ficheros):
                os.mkdir(ficheros)


            msj='Los datos se guardaron correctamente.' 
            messages.add_message(request, messages.SUCCESS, msj)
            return HttpResponseRedirect('/registro-cliente/')
        else:
            msj='Error '
            messages.add_message(request, messages.ERROR, msj)
            return HttpResponseRedirect('/registro-cliente/')     
    else:
        userForm=UserForm()  
        perfilForm=PerfilUserviews()
        ClienteForm=ClienteViews()
        a=True
        ctx={
        'p':perfilForm,
        'u':userForm,
        'c':ClienteForm,
        'activoc':a
        }      
        return render_to_response('registro_usuario.html', ctx, context_instance = RequestContext(request))

@login_required(login_url="/")       
def consulta_clientes(request):
  objclientes=Cliente.objects.filter(Usuario__User__is_active=True)
  a=True
  ctx={
  'clientes':objclientes,
  'activocc':a,
  }
  return render_to_response('consulta_cliente.html',ctx, context_instance=RequestContext(request))

@login_required(login_url="/")
def actualizar_cliente(request,id_cliente):
    try:
        objcliente = Cliente.objects.get(pk=id_cliente,Usuario__User__is_active=True)
        objusuario = Usuarios.objects.get(id=objcliente.Usuario_id)
        objuser = User.objects.get(pk=objusuario.User_id,is_active=True)
        

    except ObjectDoesNotExist:
        return HttpResponseRedirect('/validacion-login/')
    
    if request.method == 'POST':
        userForm=UserFormedit(request.POST,instance=objuser) 
        perfilForm=PerfilUsersave(request.POST,instance=objusuario)
        ClienteSaveForm = ClienteSave(request.POST,instance=objcliente)
        if userForm.is_valid() and perfilForm.is_valid() and ClienteSaveForm.is_valid():
            
            userForm.save()
            perfilForm.save()
            ClienteSaveForm.save()
    
            msj='Los datos se guardaron correctamente.' 
            messages.add_message(request, messages.SUCCESS, msj)
            return HttpResponseRedirect('/consultar-cliente-general/')
        else:
            msj='Error '
            messages.add_message(request, messages.ERROR, msj)
            return HttpResponseRedirect('/actualizar-cliente/'+id_cliente+'/')     
    else:
        userForm=UserFormedit(instance=objuser)  
        perfilForm=PerfilUserEdit(objusuario,instance=objusuario)
        ClienteForm=ClienteEdit(objcliente,instance=objcliente)
        a=True

        ctx={
        'u':userForm,
        'p':perfilForm,
        'c':ClienteForm,
        'activoc':a,
        'vactualizar':a,
        }      
        return render_to_response('registro_usuario.html', ctx, context_instance = RequestContext(request))

@login_required(login_url="/")
def suspender_cliente(request,id_cliente):
    try:
        objcliente = Cliente.objects.get(pk=id_cliente)
        objusuario = Usuarios.objects.get(id=objcliente.Usuario_id)
        objuser = User.objects.get(pk=objusuario.User_id)
        

    except ObjectDoesNotExist:
        return HttpResponseRedirect('/validacion-login/')

    User.objects.filter(pk=objusuario.User_id).update(is_active=False)
    
    objclientes=Cliente.objects.all()
    a=True
    b=False
    ctx={
    'clientes':objclientes,
    'activoc':a,
    'upload':b,
    }
    return render_to_response('consulta_cliente.html',ctx, context_instance=RequestContext(request))


@login_required(login_url="/")
def activar_cliente(request,id_cliente):
    try:
        objcliente = Cliente.objects.get(pk=id_cliente)
        objusuario = Usuarios.objects.get(id=objcliente.Usuario_id)
        objuser = User.objects.get(pk=objusuario.User_id)
        

    except ObjectDoesNotExist:
        return HttpResponseRedirect('/validacion-login/')

    print objusuario.User_id
    User.objects.filter(pk=objusuario.User_id).update(is_active=True)
    
    objclientes=Cliente.objects.all()
    a=True
    ctx={
    'clientes':objclientes,
    'activoc':a,
    }
    return render_to_response('consulta_cliente.html',ctx, context_instance=RequestContext(request))

@login_required(login_url="/")
def propiedades_cliente(request,id_cliente):
    from time import mktime
    from os import listdir
    from os.path import isfile, join
    hoyf= datetime.datetime.now()
    y = str(hoyf.year)
    m = str(hoyf.month)
    dy = str(hoyf.day)

    def to_datetime(s):
        return datetime.datetime(*time.strptime(s, "%d/%m/%Y")[0:6])

    diahoy=dy+"/"+m+"/"+y
    dhoy=to_datetime(diahoy) #dia actual
    #dhoyb=to_datetime(diahoy)+timedelta(days=1) #dia actual
    #print dhoyb

    

    try:
        objcliente = Cliente.objects.get(pk=id_cliente,Usuario__User__is_active=True)
        objusuario = Usuarios.objects.get(id=objcliente.Usuario_id)
        objuser = User.objects.get(pk=objusuario.User_id,is_active=True)
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/validacion-login/')

    #consultamos el rfc para buscar al directorio por el rfc
    vrfc = objcliente.rfc

    ficheros = "C:/proyectos/factura/factura/archivos/documentos/"+str(vrfc)#insertamos el rfc para buscar al directorio
    nvficheros = str(ficheros)
    nvficheros = str(""+nvficheros+"/")
    #print nvficheros

    if os.path.exists(ficheros):#si existe ese directorio
        arrayfacturas = []
        vcolorboton = 0
        for cosa in listdir(ficheros):
            vcolorboton = vcolorboton + 1
            file_info = {}
            #print os.path.basename(cosa) #nombre completo del archivo

            #---------------------------
            vseparanombre = cosa.split(".")
            vnombre = vseparanombre[0]
            file_info['nombre'] = vnombre
            vextencion = vseparanombre[1]
            file_info['extencion'] = vextencion
            if vextencion == "pdf" or vextencion == "PDF":
                vvext = "PDF"
                file_info['vvextencion'] = vvext
            if vextencion == "xml" or vextencion == "XML":
                vvext = "XML"
                file_info['vvextencion'] = vvext
            #--------------------------

            nvficheros2 = str(""+nvficheros+""+cosa)
            vfecha = os.path.getmtime(nvficheros2)
            ffechamodif=datetime.datetime.fromtimestamp(vfecha)
            yf = str(ffechamodif.year)
            mf = str(ffechamodif.month)
            dyf = str(ffechamodif.day)
            vfechafactura =dyf+"/"+mf+"/"+yf
            vfechafactura = to_datetime(vfechafactura)+timedelta(days=90)

            file_info['fechacreacion'] = ffechamodif


            if vcolorboton <= 2:
                vcolofor = 0
                file_info['btn'] = "success"
            if vcolorboton > 2:
                vcolofor = 1
                if vcolorboton > 3:
                    vcolorboton = 0
                file_info['btn'] = "primary"
            

            if vfechafactura > dhoy:#mistras sea mayor que el dia de hoy que se muestre sumados 90 dias
                arrayfacturas.append(file_info) 

            nvficheros2 = ""
            #os.path.basename(path) Devuelve el nombre del archivo.
        objfacturas =  listdir(ficheros)   
    else:
        arrayfacturas = ""        
    

    objdoc = arrayfacturas  
    a=True
    ctx={
    'cliente':objcliente,
    'objdoc':objdoc,
    'activoc':a,
    'upload':a,
    }
    return render_to_response('propiedades_cliente.html',ctx, context_instance=RequestContext(request))
             

def download_archivos(request,name_arc,tipo_arc,id_cliente):
    try:
        objcliente = Cliente.objects.get(pk=id_cliente,Usuario__User__is_active=True)
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/validacion-login/')

    if tipo_arc == "pdf" or tipo_arc == "PDF" or tipo_arc == "xml" or tipo_arc =="XML":
        ventrada = True
    else:
        ventrada = False

    vrfc = objcliente.rfc
    ficheros = "C:/proyectos/factura/factura/archivos/documentos/"+str(vrfc)#insertamos el rfc para buscar al directorio
    nvficheros = str(ficheros)
    

    vnombre=str(""+name_arc+"."+tipo_arc)
    nvficheros = str(""+nvficheros+"/"+vnombre)

    url = nvficheros    

    if ventrada:#si no insertar otro valor para el documetos
        if tipo_arc == "pdf" or tipo_arc == "PDF":
            response = HttpResponse(mimetype='application/pdf')
        if tipo_arc == "xml" or tipo_arc == "XML":
            response = HttpResponse(mimetype='application/xml')

        
        response['Content-Disposition'] = 'attachment; filename='+vnombre+''    
        with open(url, 'rb') as fichero:
            contenido = fichero.read()
        response.write(contenido)
        return response
    else:
        return HttpResponseRedirect('/validacion-login/')
    

def admin_cliente(request):
    from time import mktime
    from os import listdir
    from os.path import isfile, join

    idUser=request.user.id

    hoyf= datetime.datetime.now()
    y = str(hoyf.year)
    m = str(hoyf.month)
    dy = str(hoyf.day)

    def to_datetime(s):
        return datetime.datetime(*time.strptime(s, "%d/%m/%Y")[0:6])

    diahoy=dy+"/"+m+"/"+y
    dhoy=to_datetime(diahoy) #dia actual

    

    try:
        objusuario = Usuarios.objects.get(User__id=idUser)
        objcliente = Cliente.objects.get(Usuario__id=objusuario.id,Usuario__User__is_active=True)
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/validacion-login/')

    #consultamos el rfc para buscar al directorio por el rfc
    vrfc = objcliente.rfc

    ficheros = "C:/proyectos/factura/factura/archivos/documentos/"+str(vrfc)#insertamos el rfc para buscar al directorio
    nvficheros = str(ficheros)
    nvficheros = str(""+nvficheros+"/")
    #print nvficheros

    if os.path.exists(ficheros):#si existe ese directorio
        arrayfacturas = []
        vcolorboton = 0
        for cosa in listdir(ficheros):
            vcolorboton = vcolorboton + 1
            file_info = {}
            #print os.path.basename(cosa) #nombre completo del archivo

            #---------------------------
            vseparanombre = cosa.split(".")
            vnombre = vseparanombre[0]
            file_info['nombre'] = vnombre
            vextencion = vseparanombre[1]
            file_info['extencion'] = vextencion
            if vextencion == "pdf" or vextencion == "PDF":
                vvext = "PDF"
                file_info['vvextencion'] = vvext
            if vextencion == "xml" or vextencion == "XML":
                vvext = "XML"
                file_info['vvextencion'] = vvext
            #--------------------------

            nvficheros2 = str(""+nvficheros+""+cosa)
            vfecha = os.path.getmtime(nvficheros2)
            ffechamodif=datetime.datetime.fromtimestamp(vfecha)
            yf = str(ffechamodif.year)
            mf = str(ffechamodif.month)
            dyf = str(ffechamodif.day)
            vfechafactura =dyf+"/"+mf+"/"+yf
            vfechafactura = to_datetime(vfechafactura)+timedelta(days=90)
            file_info['fechacreacion'] = ffechamodif

            if vcolorboton <= 2:
                vcolofor = 0
                file_info['btn'] = "success"
            if vcolorboton > 2:
                vcolofor = 1
                if vcolorboton > 3:
                    vcolorboton = 0
                file_info['btn'] = "primary" 
     

                    
            

            if vfechafactura > dhoy:#mistras sea mayor que el dia de hoy que se muestre sumados 90 dias
                arrayfacturas.append(file_info)  
            nvficheros2 = ""
            #os.path.basename(path) Devuelve el nombre del archivo.
        objfacturas =  listdir(ficheros)   
    else:
        arrayfacturas = ""        
    

    objdoc = arrayfacturas

    objarchivos=Archivos.objects.filter(status=True).order_by('-id')[:1] 


    a=True
    ctx={
    'cliente':objcliente,
    'objdoc':objdoc,
    'activoc':a,
    'upload':a,
    'adminclint':a,
    'objarchivos':objarchivos,
    }
    return render_to_response('cliente.html', ctx, context_instance=RequestContext(request))

  
# --------------------------------inicio del modulo consulta rfc via ajax-----------------------
#@login_required(login_url='/')
def rfsc_ajax(request):
    if request.is_ajax():
        q=request.POST['q']
        #q = request.GET.get('q')
        if q is not None:            
            resultss = Cliente.objects.filter(rfc= q).count()
            return HttpResponse(resultss,mimetype="application/javascript")   
# --------------------------------fin del modulo consulta rfc via ajax--------------------------