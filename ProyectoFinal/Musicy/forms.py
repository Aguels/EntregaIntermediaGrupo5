from cProfile import label
from django import forms
import django.contrib.auth.forms as djf

class mus(forms.Form):
    Nombre = forms.CharField(max_length=200)
    Rol = forms.CharField(max_length=200)

class registro(djf.UserCreationForm):
    username = forms.CharField(label="Usuario")
    email = forms.EmailField(label="Correo")
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita la contraseña",widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    class Meta:
        model = djf.User
        fields = ["username","email","password1","password2","first_name","last_name"]

class login(djf.AuthenticationForm):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(label="Contraseña",widget=forms.PasswordInput)
