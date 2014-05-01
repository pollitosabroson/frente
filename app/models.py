from django.db import models
from geoposition.fields import GeopositionField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Create your models here.
class Delegacion(models.Model):
	descripcion_Delegacion = models.CharField(max_length=50)

	def __unicode__(self):
		return u'%s' % self.descripcion_Delegacion

class Colonia(models.Model):
	descripcion_Colonia = models.CharField(max_length=100)
	delegacion = models.ForeignKey(Delegacion)

	def __unicode__(self):
		return u'%s' % self.descripcion_Colonia

class Delegacion_frente(models.Model):
	descripcion_Delegacion = models.CharField(max_length=50)

	def __unicode__(self):
		return u'%s' % self.descripcion_Delegacion

class Colonia_frente(models.Model):
	descripcion_Colonia = models.CharField(max_length=100)
	delegacion = models.ForeignKey(Delegacion)

	def __unicode__(self):
		return u'%s' % self.descripcion_Colonia

class Ruta(models.Model):
	numero_Ruta = models.IntegerField()
	descripcion_Ruta = models.CharField(max_length=50)
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return u'%s' % self.descripcion_Ruta

class Repartidor(models.Model):
	nombre = models.CharField(max_length=50)
	apellido_Paterno = models.CharField(max_length=50)
	apellido_Materno = models.CharField(max_length=50)
	rutas = models.ManyToManyField(Ruta)
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return u'%s' % self.nombre

class Categoria(models.Model):
	descripcion_Categoria = models.CharField(max_length= 100)
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return u'%s' % self.descripcion_Categoria

class Canal_distribucion(models.Model):
	descripcion_Distribucion = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return u'%s' % self.descripcion_Distribucion

class Subcategoria1(models.Model):
	descripcion_SubCategoria1 = models.CharField(max_length = 100)
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return u'%s' % self.descripcion_SubCategoria1

class Subcategoria2(models.Model):
	descripcion_SubCategoria2 = models.CharField(max_length = 100)
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return u'%s' % self.descripcion_SubCategoria2

class Subcategoria3(models.Model):
	descripcion_SubCategoria3 = models.CharField(max_length = 100)
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return u'%s' % self.descripcion_SubCategoria3

class Cliente(models.Model):
	nombre = models.CharField(max_length=50)
	apellido_Materno = models.CharField(max_length=50)
	apellido_Paterno = models.CharField(max_length=50)
	puesto = models.CharField(max_length=50)
	telefono = models.IntegerField(max_length=10, unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Debe de se de  10 digitos', code='Invalid number')])
	mail = models.EmailField(max_length=75)
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return u'%s' % self.nombre

class Empresa(models.Model):
	nombreEmpresa = models.CharField(max_length=100)
	calle = models.CharField(max_length=100)
	numero_Exterior = models.IntegerField()
	numero_Interior = models.CharField(max_length=50,null=True)
	Colonia = models.ForeignKey(Colonia)
	delegacion = models.ForeignKey(Delegacion)
	rutas = models.ManyToManyField(Ruta)
	cliente = models.ForeignKey(Cliente)
	categoria = models.ForeignKey(Categoria, null=True)
	subcategoria1 = models.ForeignKey(Subcategoria1, null=True)
	subcategoria2 = models.ForeignKey(Subcategoria2, null=True)
	subcategoria3 = models.ForeignKey(Subcategoria3, null=True)
	position = GeopositionField(null=True)
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return u'%s' % self.nombreEmpresa	

class Cupon(models.Model):
	cupon = models.CharField(max_length=20, unique=True)
	duracion = models.CharField(max_length=50)
	fechafinal = models.DateTimeField(null=True)
	usuariogen = models.ForeignKey(User)
	created = models.DateTimeField(auto_now_add=True)
	# usuario = models.ForeignKey(ClienteFrente, null=True)
	def __unicode__(self):
		return u'%s' % self.cupon	

class Cuponera(models.Model):
	fechainicio = models.DateField(auto_now_add=True)
	fechafinal = models.DateField()
	cliente = models.ForeignKey(Cliente)
	cupon = models.ForeignKey(Cupon)

class ClienteFrente(models.Model):
	nombre = models.CharField(max_length=50)
	apellido_Materno = models.CharField(max_length=50)
	apellido_Paterno = models.CharField(max_length=50)
	telefono = models.IntegerField(max_length=10, unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Debe de ser 10 digitos', code='Invalid number')])
	mail = models.EmailField(max_length=75)
	calle = models.CharField(max_length=100)
	numero_Exterior = models.IntegerField()
	numero_Interior = models.CharField(max_length=50, null=True)
	Colonia = models.ForeignKey(Colonia_frente)
	delegacion = models.ForeignKey(Delegacion_frente)
	rutas = models.ManyToManyField(Ruta)
	cupon = models.ForeignKey(Cupon, null=True)
	categoria = models.ForeignKey(Categoria, null=True)
	subcategoria1 = models.ForeignKey(Subcategoria1, null=True)
	subcategoria2 = models.ForeignKey(Subcategoria2, null=True)
	subcategoria3 = models.ForeignKey(Subcategoria3, null=True)
	created = models.DateTimeField(auto_now_add=True)
