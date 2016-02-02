from .models import Casas,Departamentos,Locales,NavesIndustriales,Bodega
from django import forms
from django.forms import ModelForm

class casasForm(ModelForm):
    class Meta:
        model = Casas
        fields = ('foto', 'estado', 'calle', 'numero', 'telefono', 'antiguedad', 'banos', 'recamaras', 'superficie', 'amueblado', 'tipo_terreno', 'conservacion', 'estacionamiento', 'luminosidad', 'niveles', 'titulo',)
        widgets={
           'foto': forms.ClearableFileInput(attrs={'type':'file','required':'true','class':' form-control-sm'}),
           'estado': forms.TextInput(attrs={'type':'text','required':'true','class':'form-control form-control-sm-8  col-md-2'}),
           'calle': forms.TextInput(attrs={'type':'text','required':'true','class':'form-control form-control-sm-8  col-md-2'}),
           'numero': forms.TextInput(attrs={'type':'number','required':'true','class':'form-control form-control-sm-8'}),
           'telefono': forms.TextInput(attrs={'type':'number','required':'true','class':'form-control form-control-sm-8'}),
           'antiguedad': forms.TextInput(attrs={'type':'text','required':'true','class':'form-control form-control-sm-8  col-md-2'}),
           'banos': forms.TextInput(attrs={'type':'number','required':'true','class':'form-control form-control-sm-8'}),
           'recamaras': forms.TextInput(attrs={'type':'number','required':'true','class':'form-control form-control-sm-8'}),
           'superficie': forms.TextInput(attrs={'type':'decimal','required':'true','class':'form-control form-control-sm-8'}),
           'amueblado': forms.TextInput(attrs={'type':'text','required':'true','class':'form-control form-control-sm-8  col-md-2'}),
           'tipo_terreno': forms.TextInput(attrs={'type':'text','required':'true','class':'form-control form-control-sm-8  col-md-2'}),
           'conservacion': forms.TextInput(attrs={'type':'text','required':'true','class':'form-control form-control-sm-8  col-md-2'}),
           'estacionamiento': forms.TextInput(attrs={'type':'text','required':'true','class':'form-control form-control-sm-8  col-md-2'}),
           'luminosidad': forms.TextInput(attrs={'type':'text','required':'true','class':'form-control form-control-sm-8  col-md-2'}),
           'niveles': forms.TextInput(attrs={'type':'number','required':'true','class':'form-control form-control-sm-8'}),
           'titulo': forms.TextInput(attrs={'type':'text','required':'true','class':'form-control form-control-sm-8  col-md-2'}),
        }

class departamentosForm(ModelForm):
    class Meta:
        model = Departamentos
        fields = ('foto', 'ubicacion', 'telefono', 'superficie', 'antiguedad', 'disposicion', 'balcon', 'banos', 'cantidad_pisos', 'conservacion', 'elevador', 'estacionamiento', 'horario_contacto', 'metros_jardin', 'recamaras',)
        widgets={
           'foto': forms.ClearableFileInput(attrs={'type':'file','required':'true','class':' form-control-sm'}),

        }
class localesForm(ModelForm):
    class Meta:
        model = Locales
        fields = ('foto', 'ubicacion', 'telefono', 'antiguedad', 'superficie', 'metros_frente', 'metros_fondo', 'tipo_de_obra', 'ubicacion_en_plaza', 'banos', 'conservacion', 'elevador', 'estacionamiento', 'horario_contacto', 'niveles',)

class navesIndustrialesForm(ModelForm):
    class Meta:
        model = NavesIndustriales
        fields = ('foto', 'ubicacion', 'telefono', 'antiguedad', 'metros_frente', 'banos', 'metros_cuadrados_bodega', 'metros_cuadrados_oficina', 'area_carga_descarga', 'area_maniobras', 'altura_inmueble', 'capacidad_de_carga', 'fondo', 'tipo_techo', 'niveles',)

class bodegaForm(ModelForm):
    class Meta:
        model = Bodega
        fields = ('foto', 'tipo_de_bodega', 'ubicacion', 'telefono', 'antiguedad', 'superficie', 'banos', 'estacionamiento', 'niveles', 'caracteristicas_adicionales',)

