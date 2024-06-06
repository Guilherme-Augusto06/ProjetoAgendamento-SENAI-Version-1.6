# Generated by Django 5.0.6 on 2024-06-04 16:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agendamento', '0005_alter_salas_descricao'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='salas',
            name='agendado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='salas',
            name='agendamento',
            field=models.CharField(default='Disponível', max_length=50),
        ),
        migrations.AddField(
            model_name='salas',
            name='horario',
            field=models.TimeField(blank=True, null=True),
        ),
    ]