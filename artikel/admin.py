from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import format_html

from .models import Artikel
from .forms import ArtikelForm

@admin.register(Artikel)
class ArtkelAdmin(admin.ModelAdmin):
    form = ArtikelForm
    list_display = [
        'title', 'publish'
    ]
    fields = [
        'get_review_url',
        'title', 'content',
        'cover_image_url',
        'tags', 'publish'
    ]
    readonly_fields = ['get_review_url', 'publish']

    @admin.display(description='Review')
    def get_review_url(self, obj):
        return format_html('<a href="https://teamcoding.netlify.app/artikel/{}?review=1" target="_blank">https://teamcoding.netlify.app/artikel/{}</a>', obj.slug, obj.slug)