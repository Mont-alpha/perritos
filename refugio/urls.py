from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.historia,name='historia'),
    path('donaciones/',views.donaciones,name='donaciones'),
]