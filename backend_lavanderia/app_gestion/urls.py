from django.urls import path
from . import views

urlpatterns = [
    # Ruta para la página de inicio
    path('', views.inicio, name='inicio'),

    # Rutas de Clientes
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:pk>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('clientes/ver/<int:pk>/', views.ver_cliente, name='ver_cliente'),

    # Rutas de Empleados
    path('empleados/', views.listar_empleados, name='listar_empleados'),
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/editar/<int:pk>/', views.editar_empleado, name='editar_empleado'),
    path('empleados/eliminar/<int:pk>/', views.eliminar_empleado, name='eliminar_empleado'),
    path('empleados/ver/<int:pk>/', views.ver_empleado, name='ver_empleado'),

    # Rutas de Artículos de Ropa
    path('articulos/', views.listar_articulos, name='listar_articulos'),
    path('articulos/agregar/', views.agregar_articulo, name='agregar_articulo'),
    path('articulos/editar/<int:pk>/', views.editar_articulo, name='editar_articulo'),
    path('articulos/eliminar/<int:pk>/', views.eliminar_articulo, name='eliminar_articulo'),
    path('articulos/ver/<int:pk>/', views.ver_articulo, name='ver_articulo'),

    # Rutas de Máquinas
    path('maquinas/', views.listar_maquinas, name='listar_maquinas'),
    path('maquinas/agregar/', views.agregar_maquina, name='agregar_maquina'),
    path('maquinas/editar/<int:pk>/', views.editar_maquina, name='editar_maquina'),
    path('maquinas/eliminar/<int:pk>/', views.eliminar_maquina, name='eliminar_maquina'),
    path('maquinas/ver/<int:pk>/', views.ver_maquina, name='ver_maquina'),

    # Rutas de Pedidos
    path('pedidos/', views.listar_pedidos, name='listar_pedidos'),
    path('pedidos/agregar/', views.agregar_pedido, name='agregar_pedido'),
    path('pedidos/editar/<int:pk>/', views.editar_pedido, name='editar_pedido'),
    path('pedidos/eliminar/<int:pk>/', views.eliminar_pedido, name='eliminar_pedido'),
    path('pedidos/ver/<int:pk>/', views.ver_pedido, name='ver_pedido'),

    # Rutas de Detalles de Pedidos
    path('detalles/', views.listar_detalles, name='listar_detalles'),
    path('detalles/agregar/', views.agregar_detalle, name='agregar_detalle'),
    path('detalles/editar/<int:pk>/', views.editar_detalle, name='editar_detalle'),
    path('detalles/eliminar/<int:pk>/', views.eliminar_detalle, name='eliminar_detalle'),
    path('detalles/ver/<int:pk>/', views.ver_detalle_pedido, name='ver_detalle_pedido'),

    # Rutas de Reportes Operacionales
    path('reportes/', views.listar_reportes, name='listar_reportes'),
    path('reportes/agregar/', views.agregar_reporte, name='agregar_reporte'),
    path('reportes/editar/<int:pk>/', views.editar_reporte, name='editar_reporte'),
    path('reportes/eliminar/<int:pk>/', views.eliminar_reporte, name='eliminar_reporte'),
    path('reportes/ver/<int:pk>/', views.ver_reporte, name='ver_reporte'),
]
