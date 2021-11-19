from django import forms
from django.contrib import admin

from .models import Artikel
from .forms import ArtikelForm

@admin.register(Artikel)
class ArtkelAdmin(admin.ModelAdmin):
    # form = ArtikelForm
    list_display = [
        'title', 'publish'
    ]