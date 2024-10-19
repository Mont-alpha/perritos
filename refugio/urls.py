from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.historia,name='historia'),
    path('donaciones/',views.donaciones,name='donaciones'),
    path('adopcion/',views.adopcion,name='adopcion'),
    path('dhermes_admin/', views.dhermes_admin, name='dhermes_admin'),
    path('dhermes_admin_section/', views.admin_section, name='administracion'),
]