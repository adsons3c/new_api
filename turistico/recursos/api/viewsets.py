from rest_framework.viewsets import ModelViewSet
from recursos.models import Recursos
from .serializers import RecursosSerializer

class RecursosViewSet(ModelViewSet):
    queryset = Recursos.objects.all()
    serializer_class = RecursosSerializer
