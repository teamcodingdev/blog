from django.db import models
from rest_framework import serializers

from .models import Artikel

from tag.serializers import TagSerializer


class ArtikelSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    
    class Meta:
        model = Artikel
        fields = '__all__'


class ArtikelLiteSerializer(ArtikelSerializer):
    class Meta(ArtikelSerializer.Meta):
        fields = [
            'id',
            'slug', 'title',
            'cover_image_url',
            'publish'
        ]