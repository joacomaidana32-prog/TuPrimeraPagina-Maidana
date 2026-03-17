from django import forms
from .models import Instrumento, Marca, Cliente

class InstrumentoForm(forms.ModelForm):
    class Meta:
        model = Instrumento
        fields = '__all__'

class MarcaForm(forms.ModelForm):
    class Meta:
        mdoel = Marca
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class BuscarInstrumentoForm(forms.Form):
    nombre_intrumento = forms.CharField(max_length=100, required=False, label="Buscar Intrumento")