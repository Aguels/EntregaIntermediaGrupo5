from django import forms

class FormularioMusico(forms.Form):
    Nombre = forms.CharField(max_length=200)
    Rol = forms.CharField(max_length=200)