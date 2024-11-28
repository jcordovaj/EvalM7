from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Laboratorio, DirectorGeneral, Producto

# Crear un nuevo laboratorio
class LabForm(forms.ModelForm):
    nom_lab  = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'Nombre del Laboratorio'}))
    city_lab = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'Ciudad del Laboratorio'}))
    pais_lab = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'Pais del Laboratorio'}))

    class Meta: 
        model = Laboratorio
        fields = "__all__"

# Registrar un nuevo Director General
class DireForm(forms.ModelForm):
    class Meta:
        model = DirectorGeneral
        fields = '__all__'
        widgets = {
            'lab_dire': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['lab_dire'].queryset = Laboratorio.objects.all()
        self.fields['lab_dire'].empty_label = 'Selecciona un laboratorio'
        
# Crear un producto nuevo
class ProdForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nom_prod', 'lab_prod', 'f_fabricacion', 'p_costo', 'p_venta']
        widgets = {
            'lab_prod': forms.Select(attrs={'class': 'form-control'}),
            'f_fabricacion': forms.Select(choices=Producto.anios_choices, attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['lab_prod'].queryset = Laboratorio.objects.all()
        self.fields['lab_prod'].empty_label = 'Selecciona un laboratorio'

# Registrar un nuevo usuario
class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model  = User
        fields = ("username", "email")

    def save(self, commit=True):
        user = super(RegistroUsuarioForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user