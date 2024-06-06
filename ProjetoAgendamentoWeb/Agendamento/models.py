from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # Importa o modelo de usuário do Django
from django import forms
# Create your models here.
class Senai(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=1500)
    logo = models.ImageField(upload_to='logo/')

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    idade = models.IntegerField()
    data = models.DateField(default=timezone.now)
    quartos = models.CharField(max_length=50)

from django.core.exceptions import ValidationError

from django.utils import timezone
from datetime import time


class Salas(models.Model):
    salas = models.CharField(max_length=50)
    descricao = models.TextField(max_length=50)
    equipamentos = models.CharField(max_length=50)
    agendamento = models.CharField(max_length=50, default='Disponível')
    horario = models.JSONField(default=list)  # Usando JSONField para armazenar múltiplos horários
    agendado_por = models.CharField(max_length=150, null=True, blank=True)  # Alterado para CharField

    def clean(self):
        super().clean()
        if self.horarios:
            for horario in self.horarios:
                horario_time = timezone.datetime.strptime(horario, "%H:%M").time()
                if not (timezone.datetime.strptime("07:05", "%H:%M").time() <= horario_time <= timezone.datetime.strptime("17:10", "%H:%M").time()):
                    raise ValidationError("O horário de agendamento deve ser entre 7:05 e 17:10.")

    def __str__(self):
        return self.salas
