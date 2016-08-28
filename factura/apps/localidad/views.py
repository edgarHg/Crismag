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

from factura.apps.localidad.models import*

def  vista_buscar_estados(request):
    if request.is_ajax():
        if request.method=='POST':
            id_pais=request.POST['id_pais']
            data=serializers.serialize("json",Estados.objects.all().filter(pais=id_pais).order_by('nombre'),fields=('id','nombre'))
    return HttpResponse(data,mimetype="application/javascript")

def  vista_buscar_municipios(request):
    if request.is_ajax():
        if request.method=='POST':
            id_estado=request.POST['id_estado']
            data=serializers.serialize("json",Municipios.objects.all().filter(estados=id_estado).order_by('nombre'),fields=('id','nombre'))
    return HttpResponse(data,mimetype="application/javascript")



