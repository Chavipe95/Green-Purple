from django import forms
from solicitud.models import Reportes
'''
class ReportesForm(forms.Form):
    problema = forms.CharField(label="Cual es el problema:", widget=forms.TextInput(attrs={'class':'form-control',"placeholder":"Ingresa el problema"})) 
    direccion = forms.CharField(label="Direccion que se encuentra el problema:", widget=forms.Textarea(attrs={'class':'form-control',"placeholder":"Ingresa la direccion completa"})) 
    ciudad = forms.CharField(label="Ciudad en la que se localiza:", widget=forms.TextInput(attrs={'class':'form-control',"placeholder":"Ingresa la ciudad"})) 
'''    
class ReportesForm(forms.ModelForm):
    class Meta:
        model = Reportes
        fields = ["problema", "direccion", "ciudad","archivo"]
        widgets = {
            "problema": forms.TextInput(attrs={'class':'form-control',"placeholder":"Ingresa el problema"}),
            "direccion": forms.Textarea(attrs={'class':'form-control',"placeholder":"Ingresa la direccion"}),
            "ciudad": forms.Textarea(attrs={'class':'form-control',"placeholder":"Ingresa la ciudad"}),
            "archivo": forms.FileInput(attrs={'class':'form-control'}),
            "activo": forms.CheckboxInput(),
        }

class LoginForm(forms.Form):
    usuario = forms.CharField(label="Usuario", widget= forms.TextInput(attrs={'class':"form-control","placeholder":"Ingresa su usuario"}))
    password = forms.CharField(label="Password", widget= forms.PasswordInput(attrs={'class':"form-control", "placeholder":"Ingresa su contraseña"}))