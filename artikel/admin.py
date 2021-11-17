from django.contrib import admin

from .models import Artikel

@admin.register(Artikel)
class ArtkelAdmin(admin.ModelAdmin):
    pass