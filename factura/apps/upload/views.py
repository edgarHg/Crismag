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
from factura.apps.cliente.forms import*
from factura.apps.localidad.models import*

import urllib
from django.core.files import File

import datetime 
import calendar
import time
from datetime import date, timedelta

from factura.apps.upload.models import* #bueno
from factura.apps.upload.forms import*
# Create your views here.


def uploaddoc_form(request):
    docformsave=ArFormSave()    


    a=True
    b=False
    ctx={
    'activodoc':a,
    'docformsave':docformsave,
    'upload':b,
    }
    return render_to_response('documentos.html',ctx, context_instance=RequestContext(request)) 

def upload_archivos(request):
    if request.method == 'POST':
        
        formulario = ArFormSave(request.POST, request.FILES)
        if formulario.is_valid():
            Archivoform = formulario.cleaned_data['Archivo']
            pdfform = formulario.cleaned_data['Archivo']

            if Archivoform.name.endswith(".xls") or pdfform.name.endswith(".xlsx") :
                objdoc = Archivos()
                objdoc.Archivo = Archivoform
                objdoc.save()

                msj='Archivo guardado correctamente.' 
                messages.add_message(request, messages.SUCCESS, msj)
                return HttpResponseRedirect("/uploaddoc-form/")
            else:
                msj='El archivo tiene que ser Excel.'
                messages.add_message(request, messages.ERROR, msj)
                return HttpResponseRedirect("/uploaddoc-form/")

def consultar_archivos(request):
    objarchivos=Archivos.objects.filter(status=True).order_by('-id')[:1] 


    a=True
    b=False
    ctx={
    'activodoc':a,
    'objarchivos':objarchivos,
    'upload':b,
    }
    return render_to_response('consulta_archivos.html',ctx, context_instance=RequestContext(request)) 