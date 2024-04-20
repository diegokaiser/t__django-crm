from django.urls import path
from . import views

urlpatterns = [
    # website
    path('', views.home, name='home'),
    path('login', views.log_in, name='login'),
    path('logout', views.log_out, name='logout'),
    path('registrar', views.registrar, name='register'),

    # path('sistemas', views.sistemas, name='sistemas'),

    # path('carrito-de-compra', views.cart, name='carrito-de-compra'),
    # path('carrito-de-compra/confirmacion', views.cart_confirmacion, name='carrito-de-compra/confirmacion'),
    # path('carrito-de-compra/facturacion', views.cart_facturacion, name='carrito-de-compra/facturacion'),
    # path('carrito-de-compra/facturacion/metodo-pago', views.cart_facturacion_metodo_pago, name='carrito-de-compra/facturacion/metodo-pago'),

    # path('mi-cuenta', views.cuenta, name='mi-cuenta'),
    # path('mi-cuenta/carrito', views.cuenta_carrito, name='mi-cuenta/carrito'),
    # path('mi-cuenta/colaboradores', views.cuenta_colaboradores, name='mi-cuenta/colaboradores'),
    # path('mi-cuenta/direcciones', views.cuenta_direcciones, name='mi-cuenta/direcciones'),
    # path('mi-cuenta/estado-de-cuenta', views.cuenta_estado_de_cuenta, name='mi-cuenta/estado-de-cuenta'),
    # path('mi-cuenta/lista-de-deseos', views.cuenta_lista_de_deseos, name='mi-cuenta/lista-de-deseos'),
    # path('mi-cuenta/pedidos', views.cuenta_pedidos, name='mi-cuenta/pedidos'),

    path('nosotros', views.nosotros, name='nosotros'),
    path('nosotros/contactanos', views.nosotros_contactanos, name='nosotros/contactanos'),
    path('nosotros/preguntas-frecuentes', views.nosotros_faq, name='nosotros/preguntas-frecuentes'),
    path('nosotros/quienes-somos', views.nosotros_quienes_somos, name='nosotros/quienes-somos'),
    path('nosotros/terminos-y-condiciones', views.nosotros_tyc, name='nosotros/terminos-y-condiciones'),
    path('nosotros/libro-de-reclamaciones', views.nosotros_libro, name='nosotros/libro-de-reclamaciones'),

    # path('producto', views.producto, name='producto'),

    # workarea
    # path('admin/', views.workarea, name='workarea'),

    path('subsystems/', views.subsystems, name='subsystems')
]
