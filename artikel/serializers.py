from django.db import models
from rest_framework import serializers

from .models import Artikel

from tag.serializers import TagSerializer

class AartikelSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    
    class Meta:
        model = Artikel
        fields = '__all__'