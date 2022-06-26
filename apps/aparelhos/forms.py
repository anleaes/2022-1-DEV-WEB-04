from django import forms
from .models import Aparelho

class AparelhoForm(forms.ModelForm):

    class Meta:
        model = Aparelho
        exclude = ('created_on' , 'updated_on',)