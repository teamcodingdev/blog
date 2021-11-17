from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from .models import Artikel
from .serializers import AartikelSerializer

class ArtikelViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permision_classes = [AllowAny, ]
    serializer_class = AartikelSerializer
    queryset = Artikel.objects.filter(publish=True).order_by('-create')