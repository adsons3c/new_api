from django.db import models
from recursos.models import Recursos
from comentarios.models import Comentarios


class PontoTurisco(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    recurso = models.ManyToManyField(Recursos)
    comentarios = models.ManyToManyField(Comentarios)

    def __str__(self):
        return self.nome
