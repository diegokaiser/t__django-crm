from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Website views here.
def home(request):
    return render(request, 'website/index.html', {})


def log_in(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # auth
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged!')
            return redirect('home')
        else:
            messages.success(request, 'There was an error logging in. Please try again.')
    else:
        return render(request, 'website/login/index.html', {})


def log_out(request):
    logout(request)
    return redirect('home')


def registrar(request):
    return render(request, 'website/registrar/index.html', {})


def sistemas(request):
    return render(request, 'website/sistemas/index.html', {})


def cart(request):
    return render(request, 'website/carrito-de-compra/index.html', {})


def cartConfirmacion(request):
    return render(request, 'website/carrito-de-compra/confirmacion/index.html', {})


def cartFacturacion(request):
    return render(request, 'website/carrito-de-compra/facturacion/index.html', {})


def cartFacturacionMetodoPago(request):
    return render(request, 'website/carrito-de-compra/facturacion/metodo-pago/index.html', {})


def cuenta(request):
    return render(request, 'website/mi-cuenta/index.html', {})


def cuentaCarrito(request):
    return render(request, 'website/mi-cuenta/carrito/index.html', {})


def cuentaColaboradores(request):
    return render(request, 'website/mi-cuenta/colaboradores/index.html', {})


def cuentaDirecciones(request):
    return render(request, 'website/mi-cuenta/direcciones/index.html', {})


def cuentaEstadoDeCuenta(request):
    return render(request, 'website/mi-cuenta/estado-de-cuenta/index.html', {})


def cuentaListaDeDeseos(request):
    return render(request, 'website/mi-cuenta/lista-de-deseos/index.html', {})


def cuentaPedidos(request):
    return render(request, 'website/mi-cuenta/pedidos/index.html', {})


def nosotros(request):
    return render(request, 'website/mi-cuenta/index.html', {})


def nosotrosContactanos(request):
    return render(request, 'website/contactanos/index.html', {})


def nosotrosFAQ(request):
    return render(request, 'website/preguntas-frecuentes/index.html', {})


def nosotrosQuienesSomos(request):
    return render(request, 'website/quienes-somos/index.html', {})


def nosotrosTYC(request):
    return render(request, 'website/terminos-y-condiciones/index.html', {})


def producto(request):
    return render(request, 'website/producto/index.html', {})


# Workarea views here.
#def workarea(request):
#    return render(request, 'workarea/index.html', {

#    })
