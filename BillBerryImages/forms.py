from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    name = forms.CharField(label="Nom", widget=forms.TextInput(
        attrs={"placeholder": "Entrez un nom !"}))

    class Meta:
        model = Image
        fields = [
            'name',
            'image'
        ]

