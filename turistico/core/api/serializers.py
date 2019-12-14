from rest_framework.serializers import ModelSerializer
from core.models import PontoTurisco


class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontoTurisco
        fields = ['id', 'nome', 'descricao']
