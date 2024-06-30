from django.urls import path
from . import views

urlpatterns = [
    #Vista principal (inicio.html)
    path('', views.inicio, name='inicio'),

    #Vista de Registro
    path('registro/', views.registro, name='registro'),

    #Vista de Login
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),

    #Fucion Logout
    path('logout/', views.cerrar_sesion, name='logout'),

    #Funciones de STOCK/CRUD
    path('crud/', views.crud, name='crud'),
    path('productoAdd/', views.producto_add, name='productoAdd'),
    path('productoDel/<int:pk>/', views.producto_del, name='producto_del'),
    path('producto_findEdit/<str:pk>', views.producto_findEdit, name='producto_findEdit'),
    path('productoUpdate/', views.productoUpdate, name='productoUpdate'),

    #Vista Alimentos
    path('alimento/', views.alimento_view, name='alimento'),
    #Vista Transporte
    path('transporte/', views.transporte_view, name='transporte'),
    #Vista Accesorios
    path('accesorios/', views.accesorios_view, name='accesorios'),

    #Vista Carrito
    path('carrito/', views.carro, name='carrito'),
    path('agregar_al_carro/<int:product_id>/', views.agregar_al_carro, name='agregar_al_carro'),
    path('agregar_al_carro_alimento/<int:product_id>/', views.agregar_al_carro_alimento, name='agregar_al_carro_alimento'),
    path('agregar_al_carro_transporte/<int:product_id>/', views.agregar_al_carro_transporte, name='agregar_al_carro_transporte'),
    path('agregar_al_carro_accesorios/<int:product_id>/', views.agregar_al_carro_accesorios, name='agregar_al_carro_accesorios'),
    path('carro/eliminar/<int:product_id>/', views.eliminar_del_carro, name='eliminar_del_carro'),
    path('carro/eliminar_una_unidad/<int:product_id>/', views.eliminar_una_unidad, name='eliminar_una_unidad'),

    #Vista Nosotros
    path('nosotros/', views.nosotros, name='nosotros'),
]   

