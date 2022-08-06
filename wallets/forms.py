from django import forms
from django.forms.widgets import PasswordInput, TextInput, EmailInput, FileInput, NumberInput, DateInput



class BVNForm(forms.Form): 
    bvn = forms.CharField(widget=NumberInput(attrs={'class':'form-control', 'placeholder':'Your BVN', 'required':'required'}))