
from django import forms
from .models import Complete
from .models import Incomplete



class AddcompleteForm(forms.ModelForm):
    class Meta:
        model=Complete
        fields=['pic','title','location','photo','photo1','photo2','photooptional','photooptional1','photooptional2']

class AddIncompleteForm(forms.ModelForm):
    class Meta:
        model=Incomplete
        fields=['picture','heading','place','photo','photo1','photo2','photooptional','photooptional1','photooptional2']
