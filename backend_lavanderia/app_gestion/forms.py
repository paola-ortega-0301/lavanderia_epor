from django import forms
from .models import ClienteLavanderia, EmpleadoLavanderia, ArticuloRopa, MaquinaLavanderia, PedidoLavanderia, DetallePedidoLavanderia, ReporteOperacional

class ClienteForm(forms.ModelForm):
    class Meta:
        model = ClienteLavanderia
        fields = '__all__'

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = EmpleadoLavanderia
        fields = '__all__'

class ArticuloRopaForm(forms.ModelForm):
    class Meta:
        model = ArticuloRopa
        fields = '__all__'

class MaquinaLavanderiaForm(forms.ModelForm):
    class Meta:
        model = MaquinaLavanderia
        fields = '__all__'

class PedidoLavanderiaForm(forms.ModelForm):
    class Meta:
        model = PedidoLavanderia
        fields = '__all__'

class DetallePedidoLavanderiaForm(forms.ModelForm):
    class Meta:
        model = DetallePedidoLavanderia
        fields = '__all__'

class ReporteOperacionalForm(forms.ModelForm):
    class Meta:
        model = ReporteOperacional
        fields = '__all__'
