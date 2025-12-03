from django.contrib import admin
from .models import (
    ClienteLavanderia, 
    EmpleadoLavanderia, 
    ArticuloRopa, 
    MaquinaLavanderia, 
    PedidoLavanderia, 
    DetallePedidoLavanderia, 
    ReporteOperacional
)

admin.site.register(ClienteLavanderia)
admin.site.register(EmpleadoLavanderia)
admin.site.register(ArticuloRopa)
admin.site.register(MaquinaLavanderia)
admin.site.register(PedidoLavanderia)
admin.site.register(DetallePedidoLavanderia)
admin.site.register(ReporteOperacional)