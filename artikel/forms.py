from django import forms
from django.forms import fields

from .models import Artikel


class ArtikelForm(forms.ModelForm):
    cover_image_url = forms.URLField(required=True, max_length=250)

    class Meta:
        model = Artikel
        fields = '__all__'