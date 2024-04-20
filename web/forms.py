from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    ruc = forms.NumberInput(attrs={'placeholder': ''})
    nombre_comercial = forms.CharField(label='')
    razon_social = forms.CharField(label='')
    direccion_fiscal = forms.CharField(label='')
    tipo_via = forms.Select()
    referencia = forms.CharField(label='')
    nro_dpto = forms.CharField(label='')
    dpto = forms.Select()
    prov = forms.Select()
    dist = forms.Select()
    first_name = forms.CharField(label='')
    last_name = forms.CharField(label='')
    middle_name = forms.CharField(label='')
    email = forms.EmailField(label='')
    phone = forms.NumberInput(attrs={'placeholder': '987654321'})
    job_title = forms.CharField(label='')
    password = forms.CharField(label='')
