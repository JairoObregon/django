
from django import forms
from .models import ESTUDIANTE,CURSOS
 
 
# creating a form
class ESTUDIANTEForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = ESTUDIANTE
 
        # specify fields to be used
        fields = [
            "CODALU",
            "NOMALU",
            "APEALU",
            "EDAD"
        ]

        
# creating a form
class CURSOSForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = CURSOS
 
        # specify fields to be used
        fields = [
            "CODCUR",
            "NOMCUR",
            "CREDITO"
        ]

        widgets = {
            'CODCUR': forms.TextInput(attrs={'class': 'form-control'}),
            'NOMCUR': forms.TextInput(attrs={'class': 'form-control'}),
            'CREDITO': forms.TextInput(attrs={'class': 'form-control'})
        }

