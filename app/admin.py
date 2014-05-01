from django.contrib import admin
from app.models import *

# Register your models here.
class RutaAdmin(admin.ModelAdmin):
	list_display =['descripcion_Ruta']
admin.site.register(Ruta, RutaAdmin)

class RepartidorAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'apellido_Paterno']
	search_fields = ['nombre','rutas']
admin.site.register(Repartidor, RepartidorAdmin)

class ClienteAdmin(admin.ModelAdmin):
	list_display = ['nombre',]
	list_filter = ['created']
	search_fields =['nombre','puesto','created','mail']
admin.site.register(Cliente, ClienteAdmin)

class EmpresaAdmin(admin.ModelAdmin):
	list_display = ['nombreEmpresa','delegacion']
	list_filter = ['created']
	search_fields =['nombreEmpresa','calle','delegacion','ciudad','colonia','created','subcategoria1','subcategoria2','subcategoria3']
admin.site.register(Empresa, EmpresaAdmin)

class ClienteFrenteAdmin(admin.ModelAdmin):
	list_display = ['nombre',]
	list_filter = ['created']
	search_fields =['nombre','created','mail','calle','delegacion','ciudad','colonia','created','subcategoria1','subcategoria2','subcategoria3']
admin.site.register(ClienteFrente, ClienteFrenteAdmin)

class DelegacionAdmin(admin.ModelAdmin):
	list_display = ['descripcion_Delegacion']
	list_filter =['descripcion_Delegacion']
admin.site.register(Delegacion,DelegacionAdmin)

class ColoniaAdmin(admin.ModelAdmin):
	list_display = ['descripcion_Colonia']
	list_filter =['descripcion_Colonia']
admin.site.register(Colonia,ColoniaAdmin)

class DelegacionFrenteAdmin(admin.ModelAdmin):
	list_display = ['descripcion_Delegacion']
	list_filter =['descripcion_Delegacion']
admin.site.register(Delegacion_frente,DelegacionAdmin)

class ColoniafrenteAdmin(admin.ModelAdmin):
	list_display = ['descripcion_Colonia']
	list_filter =['descripcion_Colonia']
admin.site.register(Colonia_frente,ColoniaAdmin)

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ['descripcion_Categoria']
	list_filter =['descripcion_Categoria']
	search_fields = ['descripcion_Categoria','created']
admin.site.register(Categoria,CategoriaAdmin)

class Canal_distribucionAdmin(admin.ModelAdmin):
	list_display = ['descripcion_Distribucion']
	list_filter =['descripcion_Distribucion']
	search_fields = ['descripcion_Distribucion','created']
admin.site.register(Canal_distribucion,Canal_distribucionAdmin)

class Subcategoria1Admin(admin.ModelAdmin):
	list_display = ['descripcion_SubCategoria1']
	list_filter =['descripcion_SubCategoria1']
	search_fields = ['descripcion_SubCategoria1','created']
admin.site.register(Subcategoria1,Subcategoria1Admin)

class Subcategoria2Admin(admin.ModelAdmin):
	list_display = ['descripcion_SubCategoria2']
	list_filter =['descripcion_SubCategoria2']
	search_fields = ['descripcion_SubCategoria2','created']
admin.site.register(Subcategoria2,Subcategoria2Admin)

class Subcategoria3Admin(admin.ModelAdmin):
	list_display = ['descripcion_SubCategoria3']
	list_filter =['descripcion_SubCategoria3']
	search_fields = ['descripcion_SubCategoria3','created']
admin.site.register(Subcategoria3,Subcategoria3Admin)

class CuponAdmin(admin.ModelAdmin):
	list_display =['cupon','usuariogen']
	list_filter = ['cupon','usuariogen']
	search_fields = ['cupon','created','usuariogen']
admin.site.register(Cupon,CuponAdmin)

class CuponeraAdmin(admin.ModelAdmin):
	list_display =['fechainicio','fechafinal']
	list_filter = ['fechainicio','fechafinal','cliente','cupon']
	search_fields = ['fechainicio','fechafinal','cliente','cupon']
admin.site.register(Cuponera,CuponeraAdmin)