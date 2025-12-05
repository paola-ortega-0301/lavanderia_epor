from django import forms
from .models import ClienteLavanderia, EmpleadoLavanderia, ArticuloRopa, MaquinaLavanderia, PedidoLavanderia, DetallePedidoLavanderia, ReporteOperacional
from .fields import CustomDateField

class ClienteForm(forms.ModelForm):
    fecha_registro = CustomDateField()
    class Meta:
        model = ClienteLavanderia
        fields = '__all__'
        widgets = {
            'fecha_registro': forms.DateInput(attrs={'type': 'date'}),
        }

class EmpleadoForm(forms.ModelForm):
    fecha_contratacion = CustomDateField()
    class Meta:
        model = EmpleadoLavanderia
        fields = '__all__'
        widgets = {
            'fecha_contratacion': forms.DateInput(attrs={'type': 'date'}),
        }

class ArticuloRopaForm(forms.ModelForm):
    class Meta:
        model = ArticuloRopa
        fields = '__all__'

class MaquinaLavanderiaForm(forms.ModelForm):
    ultima_revision = CustomDateField()
    class Meta:
        model = MaquinaLavanderia
        fields = '__all__'
        widgets = {
            'ultima_revision': forms.DateInput(attrs={'type': 'date'}),
        }

class PedidoLavanderiaForm(forms.ModelForm):
    fecha_entrega_estimada = CustomDateField()
    fecha_entrega_real = CustomDateField()
    class Meta:
        model = PedidoLavanderia
        fields = '__all__'
        widgets = {
            'fecha_entrega_estimada': forms.DateInput(attrs={'type': 'date'}),
            'fecha_entrega_real': forms.DateInput(attrs={'type': 'date'}),
        }

class DetallePedidoLavanderiaForm(forms.ModelForm):
    maquinas = forms.ModelMultipleChoiceField(
        queryset=MaquinaLavanderia.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = DetallePedidoLavanderia
        fields = '__all__'

class ReporteOperacionalForm(forms.ModelForm):
    fecha_reporte = CustomDateField()
    class Meta:
        model = ReporteOperacional
        fields = '__all__'
        widgets = {
            'fecha_reporte': forms.DateInput(attrs={'type': 'date'}),
        }
