# Generated by Django 5.0.6 on 2024-06-06 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agendamento', '0007_remove_salas_corredor_remove_salas_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salas',
            name='agendado_por',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]