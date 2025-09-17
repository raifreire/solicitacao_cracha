from django.db import models

from datetime import datetime

from django.contrib.auth.models import User

class Cracha(models.Model):

    OPCOES_CATEGORIA = [
        ("REPRESENTANTE","REPRESENTANTE COMERCIAL"),
        ("ESTAGIARIO","ESTAGIARIO"),
        ("ESTAGIARIA","ESTAGIARIA"),
        ("ASSISTENTE_ADMINISTRATIVO","ASSISTENTE ADMINISTRATIVO"),
        ("ASSISTENTE_ADMINISTRATIVA","ASSISTENTE ADMINISTRATIVA"),
        ("ASSISTENTE_DE_RH","ASSISTENTE DE RH"),
        ("AUXILIAR_DE_MANUTENCAO","AUXILIAR DE MANUTENÇÃO"),
        ("AUXILIAR_DE_SERVIÇOS_GERAIS","AUXILIAR DE SERVIÇOS GERAIS"),
        ("COORDENADORA_DE_DEPARTAMENTO","COORDENADORA DE DEPARTAMENTO"),
        ("GERENTE_ADMINISTRATIVO","GERENTE ADMINISTRATIVO"),
        ("GERENTE_COMERCIAL","GERENTE COMERCIAL"),
        ("GERENTE_DE_DEPARTAMENTO","GERENTE DE DEPARTAMENTO"),
        ("GERENTE_DE_RECURSOS_HUMANOS","GERENTE DE RECURSOS HUMANOS"),
        ("OFICCE_BOY","OFICCE BOY"),
        ("PORTEIRO","PORTEIRO"),
        ("SUPERVISOR_ADMINISTRATIVO","SUPERVISOR ADMINISTRATIVO"),
        ("SUPERVISOR_COMERCIAL","SUPERVISOR COMERCIAL"),
        ("SUPERVISOR_DE_DEPARTAMENTO","SUPERVISOR DE DEPARTAMENTO"),
        ("SUPERVISOR_FINANCEIRO","SUPERVISOR FINANCEIRO"),
        ("SUPERVISORA_DE_DEPARTAMENTO","SUPERVISORA DE DEPARTAMENTO"),
        ("ASSISTENTE_DE_INFORMATICA","ASSISTENTE DE INFORMÁTICA"),
    ]
    OPCOES_STATUS = [ 
        ("SOLICITADO", "SOLICITADO"),
        ("EM_PRODUCAO","EM PRODUÇÃO"),
        ("PENDENTE", "PENDENTE"),
        ("CONFECCIONADO", "CONFECCIONADO")
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    nome_completo = models.CharField(max_length=150, null=False, blank=False)
    rg = models.CharField(max_length=150, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=True)
    data_cracha = models.DateTimeField(default=datetime.now, blank=False)
    funcao = models.TextField(max_length=150, choices=OPCOES_CATEGORIA, default='')
    status = models.CharField(max_length=100, choices=OPCOES_STATUS, default='' )
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user'
    )

    def __str__(self):
        return self.nome
    
