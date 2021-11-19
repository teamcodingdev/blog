from django import forms
from tinymce.widgets import TinyMCE

from .models import Artikel


class ArtikelForm(forms.ModelForm):
    # content = forms.TextInput(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Artikel
        fields = '__all__'