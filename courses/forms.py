from django import forms
from django.contrib.auth.models import User
from .models import Klasa, Lendet, Lesson



class KlasaForm(forms.ModelForm):
    class Meta:
        model = Klasa
        fields = '__all__'
        help_texts = {
            'titulli': 'Psh. Klasa 11 ose Klasa e Informatikes',
            'pershkrimi':'Vendos nje pershkrim te shkurte te klases',
            'imazhi':'Mund te vendosesh nje fotografi e klases ose mund te lihet bosh'
        }

class LendaForm(forms.ModelForm):
    class Meta:
        model = Lendet
        fields = ['krijues','slug', 'titulli', 'klasa', 'pershkrimi', 'imazhi_lendes']
        help_texts = {
            'titulli': 'Psh. Matematika, Gjeografi etj',
            'pershkrimi':'Vendos nje pershkrim te shkurte te lendes',
            'klasa':'Zhgjidhni klasen per te cilen do te krijoni lenden',
            'imazhi_lendes':'Mund te vendosesh nje fotografi e lendes ose mund te lihet bosh'
        }
        labels = {
            'titulli':'Titulli i lendes'
        }
        widgets = {'krijues': forms.HiddenInput(), 'slug': forms.HiddenInput()}


class MesimiForm(forms.ModelForm):
    class Meta:
        model = Lesson 
        fields = ['slug','titulli', 'lenda', 'video_id', 'pozicioni', ]
        help_texts = {
            'titulli':'Vendosni titullin e mesimit',
            'lenda':'Zgjidhni lenden per te cilen i perket ky mesim',
            'video_id':'Vendosni ID e videos nga Youtube te cilen do te ngarkoni (<a href="/media/youtube_help.png">ku mund ta gjej ID</a>)',
            'pozicioni':'Vendosni numrin e pozicionit ose radhen e mesimit '
        }
        widgets = {
            'slug': forms.HiddenInput()
        }