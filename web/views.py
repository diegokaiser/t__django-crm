from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Brand, Reason, BannerDestacado, BannerA, System, Subsystem, MenuCategory, MenuSubcategory, Product


# Website views here.
def home(request):
    systems = System.objects.all()
    banners_d = BannerDestacado.objects.all()
    banners_a = BannerA.objects.all()
    brands = Brand.objects.all()
    products = Product.objects.all()[:6]
    reasons = Reason.objects.all()
    return render(
        request,
        'website/index.html',
        {
            'systems': systems,
            'banners_d': banners_d,
            'banners_a': banners_a,
            'brands': brands,
            'products': products,
            'reasons': reasons
        }
    )


def load_menu(request):
    categories = MenuCategory.objects.all()
    subcategories = MenuSubcategory.objects.all()


def subsystems(request):
    system = request.GET.get('systems')
    subsystems = Subsystem.objects.filter(system=system)
    return render(
        request,
        'website/partials/select_subsystems.html',
        {
            'subsystems': subsystems
        }
    )


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
            messages.error(request, 'There was an error logging in. Please try again.')
            return redirect('login')
    else:
        return render(request, 'website/login/index.html', {})


def log_out(request):
    logout(request)
    return redirect('home')


def registrar(request):
    if request.method == 'POST':
        ruc = request.POST['ruc']
        nombreComercial = request.POST['nombreComercial']
        razonSocial = request.POST['razonSocial']
        direccionFiscal = request.POST['direccionFiscal']
        tipoVia = request.POST['tipoVia']
        referencia = request.POST['referencia']
        nroDpto = request.POST['nroDpto']
        dpto = request.POST['dpto']
        prov = request.POST['prov']
        dist = request.POST['dist']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        middleName = request.POST['middleName']
        email = request.POST['email']
        phone = request.POST['phone']
        jobTitle = request.POST['jobTitle']
        password = request.POST['password']
    else:
        return render(request, 'website/registrar/index.html', {})


def sistemas(request):
    return render(request, 'website/sistemas/index.html', {})


def cart(request):
    return render(request, 'website/carrito-de-compra/index.html', {})


def cart_confirmacion(request):
    return render(request, 'website/carrito-de-compra/confirmacion/index.html', {})


def cart_facturacion(request):
    return render(request, 'website/carrito-de-compra/facturacion/index.html', {})


def cart_facturacion_metodo_pago(request):
    return render(request, 'website/carrito-de-compra/facturacion/metodo-pago/index.html', {})


def cuenta(request):
    return render(request, 'website/mi-cuenta/index.html', {})


def cuenta_carrito(request):
    return render(request, 'website/mi-cuenta/carrito/index.html', {})


def cuenta_colaboradores(request):
    return render(request, 'website/mi-cuenta/colaboradores/index.html', {})


def cuenta_direcciones(request):
    return render(request, 'website/mi-cuenta/direcciones/index.html', {})


def cuenta_estado_de_cuenta(request):
    return render(request, 'website/mi-cuenta/estado-de-cuenta/index.html', {})


def cuenta_lista_de_deseos(request):
    return render(request, 'website/mi-cuenta/lista-de-deseos/index.html', {})


def cuenta_pedidos(request):
    return render(request, 'website/mi-cuenta/pedidos/index.html', {})


def nosotros(request):
    return render(request, 'website/nosotros/index.html', {})


def nosotros_contactanos(request):
    return render(request, 'website/nosotros/contactanos/index.html', {})


def nosotros_faq(request):
    return render(request, 'website/nosotros/preguntas-frecuentes/index.html', {})


def nosotros_tyc(request):
    return render(request, 'website/nosotros/terminos-y-condiciones/index.html', {})


def nosotros_libro(request):
    return render(request, 'website/nosotros/libro-de-reclamaciones/index.html', {})


def producto(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'website/producto/index.html', {
        'product': product
    })


def helloworld(request):
    products = Product.objects.all()
    return render(
        request,
        'website/helloworld.html',
        {
            'products': products
        }
    )

# Workarea views here.
# def workarea(request):
#    return render(request, 'workarea/index.html', {

#    })
