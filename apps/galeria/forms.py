from django import forms

from apps.galeria.models import Cracha

class CrachaForms(forms.ModelForm):
    cpf = forms.CharField(widget=forms.TextInput(
        attrs={'minlength':'14', 'maxlength':'14', 'onkeyup': 'handleCPF(event)', 'class':'form-control'}))
    
    rg = forms.CharField(widget=forms.TextInput(
        attrs={'minlength':'12', 'maxlength':'12', 'onkeyup': 'handleRG(event)', 'class':'form-control'}))


    class Meta:
        model = Cracha
        exclude = ['publicada',]
        labels = {
            'nome':'Nome',
            'data_cracha': 'Data de registro',
            'usuario': 'Usuário',
        }
    
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'nome_completo': forms.TextInput(attrs={'class':'form-control'}),
            'rg': forms.TextInput(attrs={'class':'form-control'}),
            'cpf': forms.TextInput(attrs={'class':'form-control'}),
            'funcao': forms.Select(attrs={'class':'form-control'}),
            'foto': forms.FileInput(attrs={'class':'form-control'}),
            'data_cracha': forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'usuario': forms.Select(attrs={'class':'form-control'}),
        }
