from itertools import product
from re import template
from urllib import response 
from django.shortcuts import render, redirect
from .models import Reportes, Personas
from django.http import JsonResponse
from django.views import View
from solicitud.forms import ReportesForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from solicitud.decorators import user_has_group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


def index(request):
    context = {}
    template_name="reportes/solicitud_index.html"

    return render(request, template_name, context)

class ServidorViews(View):
    template_name="reportes/servidores.html"
    context={}
    @method_decorator(user_has_group('servidor'))
    def get(self,request):
        return render(request, self.template_name, self.context)

def editar_reporte(request):

    response={}

    id = request.POST.get('id')
    problema = request.POST.get('problema')
    direccion = request.POST.get('direccion')
    ciudad = request.POST.get('ciudad')
    reportes = Reportes.objects.get(pk=id)

    reportes.problema = problema
    reportes.direccion = direccion
    reportes.ciudad = ciudad

    reportes.save()
    response['id '] = reportes.id
    response['problema'] = reportes.problema
    response['direccion'] = reportes.direccion
    response['ciudad'] = reportes.ciudad
    
    return JsonResponse(response)



def eliminar_reporte(request):

    response={}

    id = request.POST.get('id')

    reportes = Reportes.objects.get(pk=id)
    reportes.activo = False
    reportes.save()
    response['id'] = reportes.pk
        
    return JsonResponse(response)

class ReportesView(View):
    context={}
    template_name="reportes/reporte.html"
    @method_decorator(user_has_group('ciudadano')) 
    def get(self, request):
        reportes = Reportes.objects.filter(activo=True)
        self.context["reportes"] = reportes
        self.context["formReportes"] = ReportesForm()
             
        return render(request, self.template_name, self.context)
    @method_decorator(user_has_group('ciudadano')) 
  
    def post(self, request):
        formP = ReportesForm(request.POST)
        if formP.is_valid():
            reporte = formP.save(commit=False)
            archivos = request.Files.get("archivos")
            print(archivos)
            reporte.archivos= archivos
            reporte.save()

            

        reportes = Reportes.objects.filter(activo=True)
        self.context["reportes"] = reportes
        self.context["formReportes"] = ReportesForm()
    
        return render (request, self.template_name, self.context)
    
class LoginCustomView(View):
    context={}
    template_name="reportes/login.html"
    def get(self, request):
        self.context["loginForm"] = LoginForm()
        self.context["error"] = ""
        return render (request, self.template_name, self.context)
    
    def post(self, request):
        form = LoginForm(request.POST)
        self.context["error"] = ""
        if form.is_valid():
            usuario = form.cleaned_data.get("usuario")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=usuario, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                self.context["error"] = "usuario invalido"
        self.context["loginForm"] = LoginForm()

        return render(request, self.template_name, self.context)
    
def logoutCustom(request):
    logout(request)
    return redirect('login')
    
def perfil_view(request):
    
    template_name = "reportes/perfil.html"
    context = {}
    
    usuario = User.objects.filter(username= request.user.username).first()
    persona = Personas.objects.filter(usuario__username = request.user.username).first()
    print(persona)
    '''
    persona = Personas.objects.get(usuario__username = request.user.username)
    context['persona'] = persona
    '''

    return render(request, template_name, context)
