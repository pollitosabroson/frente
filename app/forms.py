from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app.models import *
from django.conf import settings
import random

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs={'placeholder': 'Password'}))

class CreateCliente(ModelForm):

	class Meta:
		model = Cliente
		fields = ('nombre','apellido_Paterno','apellido_Materno','puesto','telefono','mail')

class CreateEmpresa(ModelForm):

	class Meta:
		model = Empresa
		fields = ('nombreEmpresa','calle','numero_Exterior','numero_Interior','Colonia','delegacion')

class CreateRuta(ModelForm):

	class Meta:
		model = Ruta
		fields = '__all__'

class CreateRepartidor(ModelForm):

	class Meta:
		model = Repartidor
		fields = '__all__'

class CreateCupon(forms.ModelForm):

	class Meta:
		model = Cupon
		fields = ('usuariogen','cupon','fechafinal')
			
class DateInput(forms.DateInput):
    input_type = 'date'

class CreateClienteFrente(forms.ModelForm):
	class Meta:
		model = ClienteFrente
		fields = ('nombre','apellido_Paterno','apellido_Materno', 'cumpleanos', 'telefono','mail','calle','numero_Exterior','numero_Interior','delegacion','Colonia','entregas','cupon')
		widgets = {
            'cumpleanos': DateInput(),
            'entregas': forms.RadioSelect(),
        }

class updateCupon(ModelForm):

	class Meta:
		model = Cupon
		fields = ('usuariogen','cupon','fechafinal')