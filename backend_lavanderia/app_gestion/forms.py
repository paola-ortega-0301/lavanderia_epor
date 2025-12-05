from django import forms
from .models import (
    ClienteLavanderia, EmpleadoLavanderia, ArticuloRopa, MaquinaLavanderia, 
    PedidoLavanderia, DetallePedidoLavanderia, ReporteOperacional
)

class ClienteForm(forms.ModelForm):
    class Meta:
        model = ClienteLavanderia
        fields = '__all__'

class EmpleadoForm(forms.ModelForm):
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
    class Meta:
        model = MaquinaLavanderia
        fields = '__all__'
        widgets = {
            'ultima_revision': forms.DateInput(attrs={'type': 'date'}),
        }

class PedidoLavanderiaForm(forms.ModelForm):
    fecha_entrega_estimada = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d']
    )
    # El campo de fecha de entrega real puede estar vacío
    fecha_entrega_real = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d'],
        required=False
    )

    class Meta:
        model = PedidoLavanderia
        fields = '__all__'

class DetallePedidoLavanderiaForm(forms.ModelForm):
    maquinas = forms.ModelMultipleChoiceField(
        queryset=MaquinaLavanderia.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = DetallePedidoLavanderia
        fields = '__all__'

class ReporteOperacionalForm(forms.ModelForm):
    class Meta:
        model = ReporteOperacional
        fields = '__all__'
        widgets = {
            'fecha_reporte': forms.DateInput(attrs={'type': 'date'}),
        }
