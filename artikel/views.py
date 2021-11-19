from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from .models import Artikel
from .serializers import ArtikelSerializer, ArtikelLiteSerializer

class ArtikelViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = ArtikelSerializer
    queryset = Artikel.objects.filter(publish=True).order_by('-create')
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'


    def get_serializer_class(self):
        if self.action == 'list':
            return ArtikelLiteSerializer
        return super().get_serializer_class()