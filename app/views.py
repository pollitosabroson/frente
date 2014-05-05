from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.context_processors import csrf
from datetime import tzinfo, timedelta, datetime
from app.forms import *
import random

@login_required(login_url='/accounts/login/')
def home(request):
    print request.user.groups.filter(name='Frente').count() >= 1
    if request.user:
        if request.user.groups.filter(name='Frente').count() >= 1:
            return redirect('frente')
        elif request.user.groups.filter(name='MasxMas').count() >= 1:
            return redirect('masxmas')
        elif request.user.groups.filter(name='PR').count() >= 1:
            return redirect('pr')
        elif request.user.groups.filter(name='distribucion').count() >= 1:
            return redirect('distribucion')
    else:
        template = "home.html"
        return render_to_response(template, context_instance=RequestContext(request))

def user_login(request):
    form = LoginForm()
    if request.method == "POST":
    	form = LoginForm(request.POST)
    	if form.is_valid():
    		usuario = form.cleaned_data['username']
    		password = form.cleaned_data['password']
    		user = authenticate(username=usuario, password=password)
    		if user is not None:
    			if user.is_active:
    				login(request, user)
    				return HttpResponseRedirect('/')
    			else:
    				ctx = {"form":form, "mensaje": "Usuario Inactivo"}
    				return render_to_response("login.html",ctx, context_instance=RequestContext(request))
    		else:
    			ctx = {"form":form, "mensaje": "Datos incorrecto"}
    			return render_to_response("login.html",ctx, context_instance=RequestContext(request))	
 
    ctx = {"form":form, "mensaje":""}
    return render_to_response("login.html",ctx, context_instance=RequestContext(request))

# User Logout View
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# User Register View
def user_register(request):
    if request.user.is_anonymous():
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid:
                form.save()
                return HttpResponse('User created succcessfully.')
        else:
            form = UserRegisterForm()
        context = {}
        context.update(csrf(request))
        context['form'] = form
        #Pass the context to a template
        return render_to_response('register.html', context)
    else:
        form = UserRegisterForm()
        ctx = {"form":form, "mensaje":""}
        return render_to_response("register.html",ctx, context_instance=RequestContext(request))

def register_cliente(request):
    if request.method == "POST":
        form_a = CreateCliente(request.POST, prefix="cli")
        form_b = CreateEmpresa(request.POST, prefix="emp")
        if form_a and form_b.is_valid():
            cliente = form_a.save()
            empresa = form_b.save(commit=False)
            empresa.cliente = cliente
            empresa.save()
            return HttpResponse('registro Realisado')
        else:
            form_a = CreateCliente(prefix="cli")
            form_b = CreateEmpresa(prefix="emp")
        context = {}
        context.update(csrf(request))
        context['form_a'] = form_a
        context['form_b'] = form_b
        #Pass the context to a template
        return render_to_response('registercliente.html', context)
    else:
        form_a = CreateCliente(prefix="cli")
        form_b = CreateEmpresa(prefix="emp")
        return render(request, 'registercliente.html', {'form_a': form_a,'form_b': form_b})

def register_empresa(request):
    form = CreateEmpresa()
    if request.method == "POST":
        form = CreateEmpresa(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register/cliente/')
        else:
            return HttpResponse('algo salio mal')
            form = CreateEmpresa()
        context = {}
        context.update(csrf(request))
        context['form'] = form
        #Pass the context to a template
        return render_to_response('registerempresa.html', context)
    else:
        return render(request, 'registerempresa.html', {'form': form})

def register_ruta(request):
    form = CreateRuta()
    if request.method == "POST":
        form = CreateRuta(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Ruta Registrada')
        else:
            form = CreateRuta()
        context = {}
        context.update(csrf(request))
        context['form'] = form
        #Pass the context to a template
        return render_to_response('registerempresa.html', context)
    else:
        return render(request, 'registerempresa.html', {'form': form})

def register_repartidor(request):
    form = CreateRepartidor()
    if request.method == "POST":
        form = CreateRepartidor(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Repartidor Registrado')
        else:
            form = CreateRepartidor()
        context = {}
        context.update(csrf(request))
        context['form'] = form
        #Pass the context to a template
        return render_to_response('registerempresa.html', context)
    else:
        return render(request, 'registerempresa.html', {'form': form})

def register_cupon(request):
    startdate = datetime.today()
    enddate= startdate + timedelta(90)
    code = ''.join([random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for x in range(4)])
    form = CreateCupon(initial={'cupon': code, 'fechafinal': enddate})
    if request.method == "POST":
        form = CreateCupon(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            form = CreateCupon()
        context = {}
        context.update(csrf(request))
        context['form'] = form
        #Pass the context to a template
        return render_to_response('cupones.html', context)
    else:
        return render(request, 'cupones.html', {'form': form})

def register_frente(request):
    form = CreateClienteFrente()
    if request.method == "POST":
        form = CreateClienteFrente(request.POST)
        if form.is_valid():
            cuponvalid= form.cleaned_data['cupon']
            cupon_valid = Cupon.objects.filter(cupon = cuponvalid).exists()
            if cupon_valid  == True:
                form.save()
                return HttpResponse('Gracias por registrarte en Frente pronto empezaras recibir tu beneficios')
            else:
                ctx = {"form":form, "mensaje": "Cupon Invalido favor de comunicarte con tu proovedor por otro cupon"}
                return render_to_response("login.html",ctx, context_instance=RequestContext(request))
        else:
            print "porque perros no entra"
        context = {}
        context.update(csrf(request))
        context['form'] = form
        #Pass the context to a template
        return render_to_response('frenteregistro.html', context)
    else:
        print "porque perros no entra ultimo"
        return render(request, 'frenteregistro.html', {'form': form})