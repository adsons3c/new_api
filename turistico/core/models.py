from django.db import models
from recursos.models import Recursos
from comentarios.models import Comentarios
from avaliacoes.models import Avaliacao
from enderecos.models import Enderecos


class PontoTurisco(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    recurso = models.ManyToManyField(Recursos)
    comentarios = models.ManyToManyField(Comentarios)
    avaliacoes = models.ManyToManyField(Avaliacao)
    enderecos = models.ForeignKey(Enderecos, on_delete=models.CASCADE)


    def __str__(self):
        return self.nome
