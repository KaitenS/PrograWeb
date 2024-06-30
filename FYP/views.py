from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
# Create your views here.

#Importar modelos de alumno
from .models import tipo_producto, Producto

def inicio(request):
    productos = Producto.objects.all()
    context = {"productos": productos}
    return render(request, 'inicio.html', context)

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('inicio')  # Cambia 'inicio' por la URL a la que quieres redirigir
    else:
        form = UserCreationForm()

    return render(request, 'registro.html', {'form': form})

def inicio_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('inicio')

    else:
        form = AuthenticationForm()

    return render(request, 'inicio_sesion.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')

#Funcion para la vista STOCK/CRUD
def crud(request):
    productos = Producto.objects.all()
    context = {"productos": productos}
    #return render(request, 'productos/stock.html', context)
    return render(request, 'stock.html', context)

def producto_add(request):
    if request.method != "POST":
        productos = Producto.objects.all()
        context = {"productos": productos}
        return render(request, 'FYP/productoAdd.html', context)

    else:
        product_name   = request.POST["nombre"]
        Precio         = request.POST["precio"]
        stock          = request.POST["stock"]
        prduct_type_id = request.POST["tipo_producto"]
        product_id     = request.POST["ID"]
        product_img    = request.POST["imagen"]
    
        objTipo_Producto = tipo_producto.objects.get(prduct_type_id = tipo_producto)
        obj=Producto.objects.create(    product_name = product_name,
                                        Precio = Precio,
                                        stock = stock,
                                        prduct_type_id = prduct_type_id,
                                        product_id = product_id,
                                        product_img = product_img
                                        )
        obj.save()
        context={'mensaje': "Okey!, Producto agregado!!"}
        return render(request, 'FYP/productoAdd.html', context)
    
def producto_del(request,pk):
    context={}
    try:
        producto = Producto.objects.get(product_id=pk)

        producto.delete()
        mensaje="Bien Producto eliminado"
        productos = Producto.objects.all()
        context = {'productos': productos, 'mensaje': mensaje}
        return render(request, 'stock.html', context)
    except:
        mensaje="Error, producto no existe :C"
        productos = Producto.objects.all()
        context = {'productos': productos, 'mensaje': productos}
        return render(request, 'stock.html', context)

def producto_findEdit(request, pk):

    if pk !="":
        producto=Producto.objects.get(product_id=pk)
        tipo_productos=tipo_producto.objects.all()

        print(producto.prduct_type_id.product_type)

        context={'producto': producto, 'tipo_productos': tipo_productos}
        if producto:
            return render(request,'FYP/producto_edit.html',context)
        
def productoUpdate(request):
    if request.method == "POST":
        product_name = request.POST["nombre"]
        Precio = request.POST["precio"]
        stock = request.POST["stock"]
        prduct_type_id = request.POST.get("tipo_producto", None)  # Obtener el valor del campo tipo_producto
        product_id = request.POST["ID"]
        product_img = request.POST["imagen"]

        if prduct_type_id:
            objTipo_Producto = get_object_or_404(tipo_producto, product_type_id=prduct_type_id)

            producto = get_object_or_404(Producto, product_id=product_id)

            producto.product_name = product_name
            producto.Precio = Precio
            producto.stock = stock
            producto.prduct_type_id = objTipo_Producto

            producto.save()
            return redirect('crud')
        else:

            return HttpResponse("Tipo de producto inválido o no proporcionado")


def alimento_view(request):
    # Obtener el tipo de producto "Alimento"
    tipo_alimento = tipo_producto.objects.get(product_type='Alimento')

    # Filtrar los productos por el tipo de producto "Alimento"
    productos_alimento = Producto.objects.filter(prduct_type_id=tipo_alimento)

    context = {
        'productos': productos_alimento
    }
    return render(request, 'alimento.html', context)

def transporte_view(request):
    # Obtener el tipo de producto "Transporte"
    tipo_transporte = tipo_producto.objects.get(product_type='Transporte')

    # Filtrar los productos por el tipo de producto "Transporte"
    productos_transporte = Producto.objects.filter(prduct_type_id=tipo_transporte)

    context = {
        'productos': productos_transporte
    }
    return render(request, 'transporte.html', context)

def accesorios_view(request):
    # Obtener el tipo de producto "Accesorios"
    tipo_accesorio = tipo_producto.objects.get(product_type='Accesorios')

    # Filtrar los productos por el tipo de producto "Accesorios"
    productos_accesorios = Producto.objects.filter(prduct_type_id=tipo_accesorio)

    context = {
        'productos': productos_accesorios
    }
    return render(request, 'accesorios.html', context)


#Funcion agregar al carrito en Inicio
def agregar_al_carro(request, product_id):
    producto = get_object_or_404(Producto, product_id=product_id)
    carro = request.session.get('carro', {})

    if str(product_id) in carro:
        carro[str(product_id)]['cantidad'] += 1
    else:
        carro[str(product_id)] = {'producto': producto.product_name, 'cantidad': 1}

    request.session['carro'] = carro
    return redirect('inicio')

#Funcion agregar al carrito en Alimento
def agregar_al_carro_alimento(request, product_id):
    producto = get_object_or_404(Producto, product_id=product_id)
    carro = request.session.get('carro', {})

    if str(product_id) in carro:
        carro[str(product_id)]['cantidad'] += 1
    else:
        carro[str(product_id)] = {'producto': producto.product_name, 'cantidad': 1}

    request.session['carro'] = carro
    return redirect('alimento')

#Funcion agregar al carrito en Transporte
def agregar_al_carro_transporte(request, product_id):
    producto = get_object_or_404(Producto, product_id=product_id)
    carro = request.session.get('carro', {})

    if str(product_id) in carro:
        carro[str(product_id)]['cantidad'] += 1
    else:
        carro[str(product_id)] = {'producto': producto.product_name, 'cantidad': 1}

    request.session['carro'] = carro
    return redirect('transporte')

#Funcion agregar al carrito en accesorios
def agregar_al_carro_accesorios(request, product_id):
    producto = get_object_or_404(Producto, product_id=product_id)
    carro = request.session.get('carro', {})

    if str(product_id) in carro:
        carro[str(product_id)]['cantidad'] += 1
    else:
        carro[str(product_id)] = {'producto': producto.product_name, 'cantidad': 1}

    request.session['carro'] = carro
    return redirect('accesorios')

def carro(request):
    carro = request.session.get('carro', {})
    items = []
    for key, value in carro.items():
        product = Producto.objects.get(product_id=key)
        items.append({'producto': product, 'cantidad': value['cantidad']})
    context = {
        'carro': items
    }
    return render(request, 'carrito.html', context)

def ver_carro(request):
    productos_en_carro = []
    for item in carro.values():
        productos_en_carro.append(item)
    return render(request, 'carrito.html', {'carro': productos_en_carro})

def eliminar_del_carro(request, product_id):
    carro = request.session.get('carro', {})

    if str(product_id) in carro:
        if carro[str(product_id)]['cantidad'] > 1:
            carro[str(product_id)]['cantidad'] -= 1
        else:
            del carro[str(product_id)]

        request.session['carro'] = carro

    return redirect('carrito')

def eliminar_una_unidad(request, product_id):
    carro = request.session.get('carro', {})

    if str(product_id) in carro:
        if carro[str(product_id)]['cantidad'] > 1:
            carro[str(product_id)]['cantidad'] -= 1
        else:
            del carro[str(product_id)]

        request.session['carro'] = carro

    return redirect('carrito')

def nosotros(request):
    return render(request, 'nosotros.html')