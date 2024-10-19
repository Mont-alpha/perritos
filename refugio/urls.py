from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.historia,name='historia'),
    path('donaciones/',views.donaciones,name='donaciones'),
    path('adopcion/',views.adopcion,name='adopcion'),
    path('dhermes_admin/', views.dhermes_admin, name='dhermes_admin'),
    path('dhermes_admin_section/', views.admin_section, name='administracion'),
    path('eliminar_perrito/<int:id>/', views.eliminar_perrito, name='eliminar_perrito'),
    path('agregar_perrito/', views.agregar_perrito, name='agregar_perrito'),
]