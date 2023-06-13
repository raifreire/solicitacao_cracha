from django.db import models

from datetime import datetime

from django.contrib.auth.models import User

class Cracha(models.Model):

    OPCOES_CATEGORIA = [
        ("REPRESENTANTE","REPRESENTANTE COMERCIAL"),
        ("ESTAGIARIO","ESTAGIARIO"),
        ("ADMINISTRATIVO","ASSISTENTE ADMINISTRATIVO"),
        ("SUPERVISOR","SUPERVISOR COMERCIAL"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    nome_completo = models.CharField(max_length=150, null=False, blank=False)
    rg = models.CharField(max_length=150, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    funcao = models.TextField(max_length=150, choices=OPCOES_CATEGORIA, default='')
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=True)
    data_cracha = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user'
    )

    def __str__(self):
        return self.nome
    
