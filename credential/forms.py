from django import forms
from .models import Cad, Luxmodel, Interior
from . models import Lux


class CadForm(forms.ModelForm):
    class Meta:
        model=Cad
        fields=['name','email','phone','message',]

class LuxForm(forms.ModelForm):
    class Meta:
        model=Lux
        fields=['luximg','luximgs','luximgss',]
class LuxmodelForm(forms.ModelForm):
    class Meta:
        model=Luxmodel
        fields=['photo','photo1','photo2','photooptional','photooptional1','photooptional2','luxtitle','luxdesc','luxloc']


class InteriorForm(forms.ModelForm):
    class Meta:
        model=Interior
        fields=['interior']