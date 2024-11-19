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
from django import forms
from django.shortcuts import get_object_or_404, redirect
from .forms import ImageForm,PerritoForm
from .models import Perrito
import os



# Create your views here.
@login_required
def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('/')  # Redirige al usuario a la página principal o a donde desees
def home(request):
    return render(request,'inicio_dhermes.html')

def historia(request):
    return render(request,'inicio_dhermes.html')
def donaciones(request):
    return render(request,'donaciones.html')

def voluntariado(request):
    return render(request,'voluntariado.html')
def alianzas(request):
    return render(request,'alianzas.html')    
    
def adopcion(request):
    data = Perrito.objects.all()
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
    # Obtener todos los perritos
    perritos = Perrito.objects.all()

    # Buscar un único perrito
    buscar = request.GET.get('buscar')
    unico_perrito = None
    if buscar:
        perritos = perritos.filter(nombre__icontains=buscar)
        if perritos.count() == 1:
            unico_perrito = perritos.first()

    # Manejar POST para guardar cambios
    if unico_perrito and request.method == "POST":
        unico_perrito.nombre = request.POST.get('nombre', unico_perrito.nombre)
        unico_perrito.edad = request.POST.get('edad', unico_perrito.edad)
        unico_perrito.tamano = request.POST.get('tamano', unico_perrito.tamano)
        unico_perrito.nivel_energia = request.POST.get('nivel_energia', unico_perrito.nivel_energia)
        unico_perrito.descripcion = request.POST.get('descripcion', unico_perrito.descripcion)

        # Manejar adopción doble
        adopcion_doble_id = request.POST.get('es_adopcion_doble')
        if adopcion_doble_id:
            unico_perrito.es_adopcion_doble = Perrito.objects.get(id=adopcion_doble_id)
        else:
            unico_perrito.es_adopcion_doble = None

        # Manejar actualización de la imagen
        if 'imagen' in request.FILES:  # Si hay una nueva imagen en el formulario
            if unico_perrito.imagen:  # Si ya existe una imagen
                # Eliminar la imagen anterior del sistema de archivos
                if os.path.exists(unico_perrito.imagen.path):
                    os.remove(unico_perrito.imagen.path)
            # Asignar la nueva imagen
            unico_perrito.imagen = request.FILES['imagen']

        # Guardar los cambios
        unico_perrito.save()
        return redirect('admin_section')

    return render(request, 'dhermes_admin_section.html', {'perritos': perritos, 'unico_perrito': unico_perrito})

@login_required
def eliminar_perrito(request,id):
    perro = get_object_or_404(Perrito,pk=id)
    perro.delete()
    return redirect('administracion')

@login_required
def agregar_perrito(request):
    class modelo_perrito(forms.ModelForm):
        class  Meta:
            model = Perrito
            fields = ['nombre', 'edad','sexo','descripcion','nivel_energia','es_adopcion_doble','tamano','imagen' ]
  

    if request.POST:
        formulario_creacion = modelo_perrito(request.POST,request.FILES)
        if formulario_creacion.is_valid():
            guardado = formulario_creacion.save()
            return redirect('administracion')
        else:
            print(formulario_creacion.errors)
            return redirect('administracion')


def lista_perritos(request):
    # Obtener todos los perritos inicialmente
    perritos = Perrito.objects.all()
    
    # Obtener los parámetros de filtrado desde el request
    buscar = request.GET.get('buscar')  # Nuevo filtro por nombre
    nivel_energia = request.GET.get('nivel_energia')
    sexo = request.GET.get('sexo')
    adopcion_doble = request.GET.get('adopcion_doble')
    tamano = request.GET.get('tamano')
    edad = request.GET.get('edad')  # Nuevo filtro de edad

    # Filtrar por nombre (búsqueda)
    if buscar:
        perritos = perritos.filter(nombre__icontains=buscar)

    # Filtrar por nivel de energía
    if nivel_energia in ['baja', 'alta']:
        perritos = perritos.filter(nivel_energia=nivel_energia)
    
    # Filtrar por sexo
    if sexo in ['macho', 'hembra']:
        perritos = perritos.filter(sexo=sexo)

    # Filtrar por adopción doble
    if adopcion_doble == 'True':
        perritos = perritos.filter(es_adopcion_doble__isnull=False)
    elif adopcion_doble == 'False':
        perritos = perritos.filter(es_adopcion_doble__isnull=True)

    # Filtrar por tamaño
    if tamano in ['pequeño', 'mediano', 'grande']:
        perritos = perritos.filter(tamano=tamano)
    
    # Filtrar por edad
    if edad:
        if edad == 'menos_1':
            perritos = perritos.filter(edad__lt=1)
        elif edad == '1_3':
            perritos = perritos.filter(edad__gte=1, edad__lte=3)
        elif edad == '4_6':
            perritos = perritos.filter(edad__gte=4, edad__lte=6)
        elif edad == 'mayor_6':
            perritos = perritos.filter(edad__gt=6)

    return render(request, 'adopcion.html', {'perritos': perritos})


def detalle_perrito(request, perrito_id):
    perrito = get_object_or_404(Perrito, id=perrito_id)
    return render(request, 'detalle_perrito.html', {'perrito': perrito})

@login_required
def editar_perrito(request, id):
    perro = get_object_or_404(Perrito, pk=id)

    if request.method == "POST":
        # Actualizar campos básicos
        perro.nombre = request.POST.get('nombre', perro.nombre)
        perro.edad = request.POST.get('edad', perro.edad)
        perro.sexo = request.POST.get('genero', perro.sexo)
        perro.descripcion = request.POST.get('descripcion', perro.descripcion)

        # Manejar la adopción doble
        adopcion_doble_id = request.POST.get('es_adopcion_doble')
        if adopcion_doble_id:
            perro.es_adopcion_doble = Perrito.objects.get(id=adopcion_doble_id)
        else:
            perro.es_adopcion_doble = None

        # Manejar la imagen si se sube una nueva
        if 'img' in request.FILES:
            if perro.imagen and os.path.exists(perro.imagen.path):
                os.remove(perro.imagen.path)
            perro.imagen = request.FILES['img']

        # Guardar cambios
        perro.save()
        return redirect('administracion')

    return redirect('administracion')
    

from django.shortcuts import render

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


