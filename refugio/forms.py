from django import forms
from .models import Perrito

class PerritoForm(forms.ModelForm):
    class Meta:
        model = Perrito
        fields = ['nombre', 'edad', 'descripcion', 'nivel_energia', 'sexo', 'tamano', 'es_adopcion_doble']
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = Perrito
        fields = ['imagen']
