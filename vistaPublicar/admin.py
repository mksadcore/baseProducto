from django.contrib import admin
from .models import Casas
from .models import Departamentos
from .models import Locales
from .models import Bodega
from .models import NavesIndustriales
from .models import Categoria

# Register your models here.

@admin.register(Casas)
class CasasPublicar(admin.ModelAdmin):
        list_display=('foto', 'estado', 'calle', 'numero', 'telefono', 'antiguedad', 'banos', 'recamaras', 'superficie', 'amueblado', 'tipo_terreno', 'conservacion', 'estacionamiento', 'luminosidad', 'niveles', 'titulo',)

@admin.register(Departamentos)
class DepartamentoPublicar(admin.ModelAdmin):
        list_display=('foto', 'ubicacion', 'telefono', 'superficie', 'antiguedad', 'disposicion', 'balcon', 'banos', 'cantidad_pisos', 'conservacion', 'elevador', 'estacionamiento', 'horario_contacto', 'metros_jardin', 'recamaras',)

@admin.register(Locales)
class LocalesPublicar(admin.ModelAdmin):
        list_display=('foto', 'ubicacion', 'telefono', 'antiguedad', 'superficie', 'metros_frente', 'metros_fondo', 'tipo_de_obra', 'ubicacion_en_plaza', 'banos', 'conservacion', 'elevador', 'estacionamiento', 'horario_contacto', 'niveles',)

@admin.register(Bodega)
class BodegaPublicar(admin.ModelAdmin):
        list_display=('foto', 'tipo_de_bodega', 'ubicacion', 'telefono', 'antiguedad', 'superficie', 'banos', 'estacionamiento', 'niveles', 'caracteristicas_adicionales',)

@admin.register(NavesIndustriales)
class NavesIndustrialesPublicar(admin.ModelAdmin):
        list_display=('foto', 'ubicacion', 'telefono', 'antiguedad', 'metros_frente', 'banos', 'metros_cuadrados_bodega', 'metros_cuadrados_oficina', 'area_carga_descarga', 'area_maniobras', 'altura_inmueble', 'capacidad_de_carga', 'fondo', 'tipo_techo', 'niveles',)

@admin.register(Categoria)
class Categorias(admin.ModelAdmin):
        list_display=('categoria',)

