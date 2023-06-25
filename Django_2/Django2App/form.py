from django import forms
from Django2App.models import ModInscripción

class FormInscripción(forms.ModelForm):
    Nombre = forms.CharField(label='Nombre', max_length=100,required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    NumeroTelefono = forms.IntegerField(label='Numero de Telefono',required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    FechaSeminario = forms.DateField(label='Fecha Seminario',required=True, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    Empresa_Institucion = forms.CharField(label='Empresa o Institucion de la que asiste', max_length=100,required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Email = forms.EmailField(label='Email',required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    Profesion = forms.CharField(label='Profesión', max_length=100,required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Observaciones = forms.CharField(label='Observaciones', widget=forms.Textarea(attrs={'rows': 4,'class': 'form-control'}), max_length=1000,required=False)
    
    class Meta:
        model = ModInscripción
        fields = '__all__'
