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


# Create your views here.

def home(request):
    return render(request,'inicio_dhermes.html')

def historia(request):
    return render(request,'historia.html')
def donaciones(request):
    return render(request,'donaciones.html')
    
