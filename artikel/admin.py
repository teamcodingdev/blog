from django.contrib import admin
from django.contrib.admin.decorators import action
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

    actions = ['publish_artikel_action']

    @admin.action(description='Publish selected artikel')
    def publish_artikel_action(self, request, queryset):
        queryset.update(publish=True)

    @admin.display(description='Review')
    def get_review_url(self, obj):
        return format_html('<a href="https://teamcoding.netlify.app/artikel/{}?review=1" target="_blank">https://teamcoding.netlify.app/artikel/{}</a>', obj.slug, obj.slug)