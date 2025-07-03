from django import forms
from .models import Parca

class ParcaForm(forms.ModelForm):
    firma_adi = forms.CharField(max_length=200, required=True, label="Firma Adı")

    class Meta:
        model = Parca
        fields = ['ad', 'adet', 'renk'] # Firma alanı buradan kaldırıldı