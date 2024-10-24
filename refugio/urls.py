from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.historia,name='historia'),
    path('donaciones/',views.donaciones,name='donaciones'),
    path('adopcion/',views.lista_perritos,name='adopcion'),
    path('dhermes_admin/', views.dhermes_admin, name='dhermes_admin'),
    path('dhermes_admin_section/', views.admin_section, name='administracion'),
    path('eliminar_perrito/<int:id>/', views.eliminar_perrito, name='eliminar_perrito'),
    path('agregar_perrito/', views.agregar_perrito, name='agregar_perrito'),
    path('perrito/<int:perrito_id>/', views.detalle_perrito, name='detalle_perrito'),
    path('editar_perrito/<int:id>/', views.editar_perrito, name='editar_perrito'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)