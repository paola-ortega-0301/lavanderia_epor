from django.shortcuts import render, redirect, get_object_or_404
from .models import ClienteLavanderia, EmpleadoLavanderia, ArticuloRopa, MaquinaLavanderia, PedidoLavanderia, DetallePedidoLavanderia, ReporteOperacional
from .forms import ClienteForm, EmpleadoForm, ArticuloRopaForm, MaquinaLavanderiaForm, PedidoLavanderiaForm, DetallePedidoLavanderiaForm, ReporteOperacionalForm

def inicio(request):
    return render(request, 'app_gestion/inicio.html')

# Vistas de Clientes
def listar_clientes(request):
    clientes = ClienteLavanderia.objects.all()
    return render(request, 'app_gestion/listar_clientes.html', {'clientes': clientes})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'app_gestion/form_cliente.html', {'form': form})

def editar_cliente(request, pk):
    cliente = get_object_or_404(ClienteLavanderia, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'app_gestion/form_cliente.html', {'form': form})

def eliminar_cliente(request, pk):
    cliente = get_object_or_404(ClienteLavanderia, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listar_clientes')
    return render(request, 'app_gestion/confirmar_eliminar.html', {'cliente': cliente})

# Vistas de Empleados
def listar_empleados(request):
    empleados = EmpleadoLavanderia.objects.all()
    return render(request, 'app_gestion/listar_empleados.html', {'empleados': empleados})

def agregar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'app_gestion/form_empleado.html', {'form': form})

def editar_empleado(request, pk):
    empleado = get_object_or_404(EmpleadoLavanderia, pk=pk)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('listar_empleados')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'app_gestion/form_empleado.html', {'form': form})

def eliminar_empleado(request, pk):
    empleado = get_object_or_404(EmpleadoLavanderia, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('listar_empleados')
    return render(request, 'app_gestion/confirmar_eliminar_empleado.html', {'empleado': empleado})

# Vistas de Articulos de Ropa
def listar_articulos(request):
    articulos = ArticuloRopa.objects.all()
    return render(request, 'app_gestion/listar_articulos.html', {'articulos': articulos})

def agregar_articulo(request):
    if request.method == 'POST':
        form = ArticuloRopaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_articulos')
    else:
        form = ArticuloRopaForm()
    return render(request, 'app_gestion/form_articulo.html', {'form': form})

def editar_articulo(request, pk):
    articulo = get_object_or_404(ArticuloRopa, pk=pk)
    if request.method == 'POST':
        form = ArticuloRopaForm(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('listar_articulos')
    else:
        form = ArticuloRopaForm(instance=articulo)
    return render(request, 'app_gestion/form_articulo.html', {'form': form})

def eliminar_articulo(request, pk):
    articulo = get_object_or_404(ArticuloRopa, pk=pk)
    if request.method == 'POST':
        articulo.delete()
        return redirect('listar_articulos')
    return render(request, 'app_gestion/confirmar_eliminar_articulo.html', {'articulo': articulo})

# Vistas de Maquinas
def listar_maquinas(request):
    maquinas = MaquinaLavanderia.objects.all()
    return render(request, 'app_gestion/listar_maquinas.html', {'maquinas': maquinas})

def agregar_maquina(request):
    if request.method == 'POST':
        form = MaquinaLavanderiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_maquinas')
    else:
        form = MaquinaLavanderiaForm()
    return render(request, 'app_gestion/form_maquina.html', {'form': form})

def editar_maquina(request, pk):
    maquina = get_object_or_404(MaquinaLavanderia, pk=pk)
    if request.method == 'POST':
        form = MaquinaLavanderiaForm(request.POST, instance=maquina)
        if form.is_valid():
            form.save()
            return redirect('listar_maquinas')
    else:
        form = MaquinaLavanderiaForm(instance=maquina)
    return render(request, 'app_gestion/form_maquina.html', {'form': form})

def eliminar_maquina(request, pk):
    maquina = get_object_or_404(MaquinaLavanderia, pk=pk)
    if request.method == 'POST':
        maquina.delete()
        return redirect('listar_maquinas')
    return render(request, 'app_gestion/confirmar_eliminar_maquina.html', {'maquina': maquina})

# Vistas de Pedidos
def listar_pedidos(request):
    pedidos = PedidoLavanderia.objects.all()
    return render(request, 'app_gestion/listar_pedidos.html', {'pedidos': pedidos})

def agregar_pedido(request):
    if request.method == 'POST':
        form = PedidoLavanderiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pedidos')
    else:
        form = PedidoLavanderiaForm()
    return render(request, 'app_gestion/form_pedido.html', {'form': form})

def editar_pedido(request, pk):
    pedido = get_object_or_404(PedidoLavanderia, pk=pk)
    if request.method == 'POST':
        form = PedidoLavanderiaForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('listar_pedidos')
    else:
        form = PedidoLavanderiaForm(instance=pedido)
    return render(request, 'app_gestion/form_pedido.html', {'form': form})

def eliminar_pedido(request, pk):
    pedido = get_object_or_404(PedidoLavanderia, pk=pk)
    if request.method == 'POST':
        pedido.delete()
        return redirect('listar_pedidos')
    return render(request, 'app_gestion/confirmar_eliminar_pedido.html', {'pedido': pedido})

# Vistas de Detalles de Pedidos
def listar_detalles(request):
    detalles = DetallePedidoLavanderia.objects.all()
    return render(request, 'app_gestion/listar_detalles.html', {'detalles': detalles})

def agregar_detalle(request):
    if request.method == 'POST':
        form = DetallePedidoLavanderiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_detalles')
    else:
        form = DetallePedidoLavanderiaForm()
    return render(request, 'app_gestion/form_detalle.html', {'form': form})

def editar_detalle(request, pk):
    detalle = get_object_or_404(DetallePedidoLavanderia, pk=pk)
    if request.method == 'POST':
        form = DetallePedidoLavanderiaForm(request.POST, instance=detalle)
        if form.is_valid():
            form.save()
            return redirect('listar_detalles')
    else:
        form = DetallePedidoLavanderiaForm(instance=detalle)
    return render(request, 'app_gestion/form_detalle.html', {'form': form})

def eliminar_detalle(request, pk):
    detalle = get_object_or_404(DetallePedidoLavanderia, pk=pk)
    if request.method == 'POST':
        detalle.delete()
        return redirect('listar_detalles')
    return render(request, 'app_gestion/confirmar_eliminar_detalle.html', {'detalle': detalle})

# Vistas de Reportes Operacionales
def listar_reportes(request):
    reportes = ReporteOperacional.objects.all()
    return render(request, 'app_gestion/listar_reportes.html', {'reportes': reportes})

def agregar_reporte(request):
    if request.method == 'POST':
        form = ReporteOperacionalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_reportes')
    else:
        form = ReporteOperacionalForm()
    return render(request, 'app_gestion/form_reporte.html', {'form': form})

def editar_reporte(request, pk):
    reporte = get_object_or_404(ReporteOperacional, pk=pk)
    if request.method == 'POST':
        form = ReporteOperacionalForm(request.POST, instance=reporte)
        if form.is_valid():
            form.save()
            return redirect('listar_reportes')
    else:
        form = ReporteOperacionalForm(instance=reporte)
    return render(request, 'app_gestion/form_reporte.html', {'form': form})

def eliminar_reporte(request, pk):
    reporte = get_object_or_404(ReporteOperacional, pk=pk)
    if request.method == 'POST':
        reporte.delete()
        return redirect('listar_reportes')
    return render(request, 'app_gestion/confirmar_eliminar_reporte.html', {'reporte': reporte})
