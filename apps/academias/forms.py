from django import forms
from .models import Academia

class AcademiaForm(forms.ModelForm):

    class Meta:
        model = Academia
        exclude = ('created_on' , 'updated_on',)