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

from .forms import ImageForm,PerritoForm
from .models import Perrito
import os



# Create your views here.

def home(request):
    return render(request,'inicio_dhermes.html')

def historia(request):
    return render(request,'historia.html')
def donaciones(request):
    return render(request,'donaciones.html')
    
    
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
    perros = Perrito.objects.all()
    lista_perros = ['Quiltro','Affenpinscher', 'Airedale terrier', 'Akita', 'Akita americano', 'Alaskan Husky', 'Alaskan malamute', 'American Foxhound', 'American pit bull terrier', 'American staffordshire terrier', 'Ariegeois', 'Artois', 'Australian silky terrier', 'Australian Terrier', 'Austrian Black & Tan Hound', 'Azawakh', 'Balkan Hound', 'Basenji', 'Basset Alpino (Alpine Dachsbracke)', 'Basset Artesiano Normando', 'Basset Azul de Gascuña (Basset Bleu de Gascogne)', 'Basset de Artois', 'Basset de Westphalie', 'Basset Hound', 'Basset Leonado de Bretaña (Basset fauve de Bretagne)', 'Bavarian Mountain Scenthound', 'Beagle', 'Beagle Harrier', 'Beauceron', 'Bedlington Terrier', 'Bichon Boloñes', 'Bichón Frisé', 'Bichón Habanero', 'Billy', 'Black and Tan Coonhound', 'Bloodhound (Sabueso de San Huberto)', 'Bobtail', 'Boerboel', 'Border Collie', 'Border terrier', 'Borzoi', 'Bosnian Hound', 'Boston terrier', 'Bouvier des Flandres', 'Boxer', 'Boyero de Appenzell', 'Boyero de Australia', 'Boyero de Entlebuch', 'Boyero de las Ardenas', 'Boyero de Montaña Bernes', 'Braco Alemán de pelo corto', 'Braco Alemán de pelo duro', 'Braco de Ariege', 'Braco de Auvernia', 'Braco de Bourbonnais', 'Braco de Saint Germain', 'Braco Dupuy', 'Braco Francés', 'Braco Italiano', 'Broholmer', 'Buhund Noruego', 'Bull terrier', 'Bulldog americano', 'Bulldog inglés', 'Bulldog francés', 'Bullmastiff', 'Ca de Bestiar', 'Cairn terrier', 'Cane Corso', 'Cane da Pastore Maremmano-Abruzzese', 'Caniche (Poodle)', 'Caniche Toy (Toy Poodle)', 'Cao da Serra de Aires', 'Cao da Serra de Estrela', 'Cao de Castro Laboreiro', 'Cao de Fila de Sao Miguel', 'Cavalier King Charles Spaniel', 'Cesky Fousek', 'Cesky Terrier', 'Chesapeake Bay Retriever', 'Chihuahua', 'Chin', 'Chow Chow', 'Cirneco del Etna', 'Clumber Spaniel', 'Cocker Spaniel Americano', 'Cocker Spaniel Inglés', 'Collie Barbudo', 'Collie de Pelo Cort', 'Collie de Pelo Largo', 'Cotón de Tuléar', 'Curly Coated Retriever', 'Dálmata', 'Dandie dinmont terrier', 'Deerhound', 'Dobermann', 'Dogo Argentino', 'Dogo de Burdeos', 'Dogo del Tibet', 'Drentse Partridge Dog', 'Drever', 'Dunker', 'Elkhound Noruego', 'Elkhound Sueco', 'English Foxhound', 'English Springer Spaniel', 'English Toy Terrier', 'Epagneul Picard', 'Eurasier', 'Fila Brasileiro', 'Finnish Lapphound', 'Flat Coated Retriever', 'Fox terrier de pelo de alambre', 'Fox terrier de pelo liso', 'Foxhound Inglés', 'Frisian Pointer', 'Galgo Español', 'Galgo húngaro (Magyar Agar)', 'Galgo Italiano', 'Galgo Polaco (Chart Polski)', 'Glen of Imaal Terrier', 'Golden Retriever', 'Gordon Setter', "Gos d'Atura Catalá", 'Gran Basset Griffon Vendeano', 'Gran Boyero Suizo', 'Gran Danés (Dogo Aleman)', 'Gran Gascón Saintongeois', 'Gran Griffon Vendeano', 'Gran Munsterlander', 'Gran Perro Japonés', 'Grand Anglo Francais Tricoleur', 'Grand Bleu de Gascogne', 'Greyhound', 'Griffon Bleu de Gascogne', 'Griffon de pelo duro (Grifón Korthals)', 'Griffon leonado de Bretaña', 'Griffon Nivernais', 'Grifon Belga', 'Grifón de Bruselas', 'Haldenstoever', 'Harrier', 'Hokkaido', 'Hovawart', 'Husky Siberiano (Siberian Husky)', 'Ioujnorousskaia Ovtcharka', 'Irish Glen of Imaal terrier', 'Irish soft coated wheaten terrier', 'Irish terrier', 'Irish Water Spaniel', 'Irish Wolfhound', 'Jack Russell terrier', 'Jindo Coreano', 'Kai', 'Keeshond', 'Kelpie australiano (Australian kelpie)', 'Kerry blue terrier', 'King Charles Spaniel', 'Kishu', 'Komondor', 'Kooiker', 'Kromfohrländer', 'Kuvasz', 'Labrador Retriever', 'Lagotto Romagnolo', 'Laika de Siberia Occidental', 'Laika de Siberia Oriental', 'Laika Ruso Europeo', 'Lakeland terrier', 'Landseer', 'Lapphund Sueco', 'Lebrel Afgano', 'Lebrel Arabe (Sloughi)', 'Leonberger', 'Lhasa Apso', 'Lowchen (Pequeño Perro León)', 'Lundehund Noruego', 'Malamute de Alaska', 'Maltés', 'Manchester terrier', 'Mastiff', 'Mastín de los Pirineos', 'Mastín Español', 'Mastín Napolitano', 'Mudi', 'Norfolk terrier', 'Norwich terrier', 'Nova Scotia duck tolling retriever', 'Ovejero alemán', 'Otterhound', 'Rafeiro do Alentejo', 'Ratonero Bodeguero Andaluz', 'Retriever de Nueva Escocia', 'Rhodesian Ridgeback', 'Ridgeback de Tailandia', 'Rottweiler', 'Saarloos', 'Sabueso de Hamilton', 'Sabueso de Hannover', 'Sabueso de Hygen', 'Sabueso de Istria', 'Sabueso de Posavaz', 'Sabueso de Schiller (Schillerstovare)', 'Sabueso de Smaland (Smalandsstovare)', 'Sabueso de Transilvania', 'Sabueso del Tirol', 'Sabueso Español', 'Sabueso Estirio de pelo duro', 'Sabueso Finlandés', 'Sabueso Francés blanco y negro', 'Sabueso Francés tricolor', 'Sabueso Griego', 'Sabueso Polaco (Ogar Polski)', 'Sabueso Serbio', 'Sabueso Suizo', 'Sabueso Yugoslavo de Montaña', 'Sabueso Yugoslavo tricolor', 'Saluki', 'Samoyedo', 'San Bernardo', 'Sarplaninac', 'Schapendoes', 'Schipperke', 'Schnauzer estándar', 'Schnauzer gigante (Riesenschnauzer)', 'Schnauzer miniatura (Zwergschnauzer)', 'Scottish terrier', 'Sealyham terrier', 'Segugio Italiano', 'Seppala Siberiano', 'Setter Inglés', 'Setter Irlandés', 'Setter Irlandés rojo y blanco', 'Shar Pei', 'Shiba Inu', 'Shih Tzu', 'Shikoku', 'Skye terrier', 'Slovensky Cuvac', 'Slovensky Kopov', 'Smoushond Holandés', 'Spaniel Alemán (German Wachtelhund)', 'Spaniel Azul de Picardía', 'Spaniel Bretón', 'Spaniel de Campo', 'Spaniel de Pont Audemer', 'Spaniel Francés', 'Spaniel Tibetano', 'Spinone Italiano', 'Spítz Alemán', 'Spitz de Norbotten (Norbottenspets)', 'Spitz Finlandés', 'Spitz Japonés', 'Staffordshire bull terrier', 'Staffordshire terrier americano', 'Sussex Spaniel', 'Teckel (Dachshund)', 'Tchuvatch eslovaco', 'Terranova (Newfoundland)', 'Terrier australiano (Australian terrier)', 'Terrier brasilero', 'Terrier cazador alemán', 'Terrier checo (Ceský teriér)', 'Terrier galés', 'Terrier irlandés (Irish terrier)', 'Terrier japonés (Nihon teria)', 'Terrier negro ruso', 'Terrier tibetano', 'Tosa', 'Viejo Pastor Inglés', 'Viejo Pointer Danés (Old Danish Pointer)', 'Vizsla', 'Volpino Italiano', 'Weimaraner', 'Welsh springer spaniel', 'Welsh Corgi Cardigan', 'Welsh Corgi Pembroke', 'Welsh terrier', 'West highland white terrier', 'Whippet', 'Wirehaired solvakian pointer', 'Xoloitzcuintle', 'Yorkshire Terrier']      
    data = {'perritos': perros,'razas': lista_perros}
    return render(request,'dhermes_admin_section.html',data)

@login_required
def eliminar_perrito(request,id):
    perro = get_object_or_404(Perrito,pk=id)
    perro.delete()
    return redirect('administracion')

@login_required
def agregar_perrito(request):
    if request.POST:
        nombre = request.POST['nombre']
        edad = request.POST['edad']
        raza = request.POST['raza']
        genero = request.POST['genero']
        tipo_casa = request.POST['tipo_casa']
        descripcion = request.POST['descripcion']
        nivel_energia = request.POST['nivel_energia']
        tamano = request.POST['tamano']
        es_adopcion_doble = request.POST.get('es_adopcion_doble', False)
        img = request.FILES.get('img')

        perro = Perrito(
            nombre=nombre,
            edad=edad,
            raza=raza,
            sexo=genero,
            tipo_casa=tipo_casa,
            descripcion=descripcion,
            nivel_energia=nivel_energia,
            tamano=tamano,
            es_adopcion_doble=es_adopcion_doble,
            imagen=img
        )
        perro.save()
        return redirect('administracion')
    else:
        return render(request,'agregar_perrito.html')


def lista_perritos(request):
    # Obtener todos los perritos inicialmente
    perritos = Perrito.objects.all()
    
    # Obtener los parámetros de filtrado desde el request
    nivel_energia = request.GET.get('nivel_energia')
    sexo = request.GET.get('sexo')
    adopcion_doble = request.GET.get('adopcion_doble')
    tamano = request.GET.get('tamano')
    edad = request.GET.get('edad')  # Nuevo filtro de edad

    # Filtrar por nivel de energía
    if nivel_energia in ['baja', 'alta']:
        perritos = perritos.filter(nivel_energia=nivel_energia)
    
    # Filtrar por sexo
    if sexo in ['macho', 'hembra']:
        perritos = perritos.filter(sexo=sexo)

    # Filtrar por adopción doble
    if adopcion_doble == 'True':
        perritos = perritos.filter(es_adopcion_doble=True)

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
    if request.POST:
        nombre = request.POST.get('nombre', perro.nombre)
        edad = request.POST.get('edad', perro.edad)
        genero = request.POST.get('genero', perro.sexo)
        descripcion = request.POST.get('descripcion', perro.descripcion)

        perro.nombre = nombre
        perro.edad = edad
        perro.sexo = genero
        perro.descripcion = descripcion
        perro.save()
            
        old_image = Perrito.objects.get(id=id)
        if 'img' in request.FILES:
            # elimina la antigua foto.
            image_path = old_image.imagen.path
            if os.path.exists(image_path):
                os.remove(image_path)
                # updating with new image
                old_image.imagen = request.FILES['img']
        
        form = ImageForm(request.POST, request.FILES, instance=old_image)
        if form.is_valid():
            form.save()
        
        return redirect('administracion')
        
        return redirect('administracion')
    else:
        return redirect('administracion')