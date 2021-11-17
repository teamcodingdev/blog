from django.db.models import base
from rest_framework import routers, urlpatterns

from . import views

router = routers.SimpleRouter()
router.register(r'artikel', views.ArtikelViewset, basename='artikel')

urlpatterns = router.urls