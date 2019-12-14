from rest_framework.viewsets import ModelViewSet
from core.models import PontoTurisco
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PontoTurisco.objects.all()
    serializer_class = PontoTuristicoSerializer
