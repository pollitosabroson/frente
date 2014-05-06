from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'frente.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app.views.home', name='home'),
    url(r'^frente/$', 'app.views.frente', name='frente'),
    url(r'^masxmas/$', 'app.views.masxmas', name='masxmas'),
    url(r'^pr/$', 'app.views.pr', name='pr'),
    url(r'^distribucion/$', 'app.views.distribucion', name='distribucion'),
    url(r'^accounts/login/$', 'app.views.user_login', name="url_login"),		
    url(r'^accounts/logout/$', 'app.views.user_logout', name="url_logout"),
    url(r'^frente/usuarionuevo/$', 'app.views.user_register', name="url_registro"),
    url(r'^masxmas/cliente/$', 'app.views.register_cliente', name="url_registrocliente"),
    url(r'^empresa/suscripcion/$', 'app.views.register_empresa', name="url_registroempresa"),
    url(r'^register/ruta/$', 'app.views.register_ruta', name="url_registroruta"),
    url(r'^register/repartidor/$', 'app.views.register_repartidor', name="url_registrorepartidor"),
    url(r'^frente/suscripcion/$', 'app.views.register_frente', name="url_registrofrente"),
    url(r'^register/cupon/$', 'app.views.register_cupon', name="url_registrocupon"),
    url(r'^frente/usuarios/$', 'app.views.frente_usuarios', name="url_frenteusuarios"),
    url(r'^frente/usuarios/edit/(?P<id>[0-9]+)$', 'app.views.edit_frenteusuarios', name="url_frenteusuarios"),
    url(r'^frente/clientes/$', 'app.views.frente_clientes', name="url_frenteuclientes"),
    # url(r'^frente/clientes/edit/(?P<id>[0-9]+)$', 'app.views.edit_frenteclientes', name="url_editfrenteclientes"),


)
