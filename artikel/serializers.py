from django.db import models
from rest_framework import serializers

from .models import Artikel

from tag.serializers import TagSerializer

import re


class ArtikelSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    duration = serializers.SerializerMethodField()
    
    class Meta:
        model = Artikel
        fields = '__all__'

    
    def get_duration(self, obj):
        c = re.sub(r'(\<[\s\w\/\"\=\-]+\>)', '', obj.content)
        return len(c.strip().split())


class ArtikelLiteSerializer(ArtikelSerializer):
    class Meta(ArtikelSerializer.Meta):
        fields = [
            'id',
            'slug', 'title',
            'cover_image_url',
            'publish'
        ]