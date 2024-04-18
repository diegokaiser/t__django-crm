from django.urls import path
from . import views

urlpatterns = [
    # workarea
    path('admin/', views.workarea, name='workarea'),
    # website
    path('', views.home, name='home'),
    # path('login', views.login, name='login'),
    # path('registrar', views.login, name='register'),
    # path('sistemas', views.sistemas, name='sistemas'),

    # path('carrito-de-compra', views.cart, name='carrito-de-compra'),
    # path('carrito-de-compra/confirmacion', views.cartConfirmacion, name='carrito-de-compra/confirmacion'),
    # path('carrito-de-compra/facturacion', views.cartFacturacion, name='carrito-de-compra/facturacion'),
    # path('carrito-de-compra/facturacion/metodo-pago', views.cartFacturacionMetodoPago, name='carrito-de-compra/facturacion/metodo-pago'),

    # path('mi-cuenta', views.cuenta, name='mi-cuenta'),
    # path('mi-cuenta/carrito', views.cuentaCarrito, name='mi-cuenta/carrito'),
    # path('mi-cuenta/colaboradores', views.cuentaColaboradores, name='mi-cuenta/colaboradores'),
    # path('mi-cuenta/direcciones', views.cuentaDirecciones, name='mi-cuenta/direcciones'),
    # path('mi-cuenta/estado-de-cuenta', views.cuentaEstadoDeCuenta, name='mi-cuenta/estado-de-cuenta'),
    # path('mi-cuenta/lista-de-deseos', views.cuentaListaDeDeseos, name='mi-cuenta/lista-de-deseos'),
    # path('mi-cuenta/pedidos', views.cuentaPedidos, name='mi-cuenta/pedidos'),

    # path('nosotros', views.nosotros, name='nosotros'),
    # path('nosotros/contactanos', views.nosotrosContactanos, name='nosotros/contactanos'),
    # path('nosotros/preguntas-frecuentes', views.nosotrosFAQ, name='nosotros/preguntas-frecuentes'),
    # path('nosotros/quienes-somos', views.nosotrosQuienesSomos, name='nosotros/quienes-somos'),
    # path('nosotros/terminos-y-condiciones', views.nosotrosTYC, name='nosotros/terminos-y-condiciones'),

    # path('producto', views.producto, name='producto'),
]
