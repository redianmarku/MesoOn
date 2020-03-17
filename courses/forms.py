from django import forms
from django.contrib.auth.models import User
from .models import Klasa



class KlasaForm(forms.ModelForm):
    class Meta:
        model = Klasa
        fields = '__all__'
        help_texts = {
            'titulli': 'Psh. Klasa 11 ose Klasa e Informatikes',
            'pershkrimi':'Vendos nje pershkrim te shkurte te klases',
            'imazhi':'Mund te vendosesh nje fotografi e klases ose mund te lihet bosh'
        }

