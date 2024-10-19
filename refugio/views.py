from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, views as auth_views
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.views.generic import DetailView
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import perritos


# Create your views here.

def home(request):
    return render(request,'inicio_dhermes.html')

def historia(request):
    return render(request,'historia.html')
def donaciones(request):
    return render(request,'donaciones.html')
    
    
def adopcion(request):
    data = perritos.objects.all()
    return render(request,'adopcion.html',{'data':data})

def dhermes_admin(request):
    data = {'error_message':''}
    if request.POST:
        username = request.POST['name_user']
        password = request.POST['password_dhermes']
        usuario_login = authenticate(request,username=username,password=password)
        if usuario_login is not None:
            login(request,usuario_login)
            return redirect('administracion')
        else:
            data['error_message'] = 'Usuario o contraseña incorrectos'
            return render(request,'dhermes_admin.html',data)
    else:
        return render(request,'dhermes_admin.html',data)

@login_required
def admin_section(request):
    return render(request,'dhermes_admin_section.html')
