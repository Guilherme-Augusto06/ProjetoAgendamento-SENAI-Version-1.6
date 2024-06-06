# forms.py
from django import forms
from .models import Salas
from django.utils import timezone
from django.contrib.auth.models import User

class formCadastroUsuario(forms.Form):
    first_name = forms.CharField(label="Nome", max_length=40)
    last_name = forms.CharField(label="Sobrenome", max_length=40)
    user = forms.CharField(label="Usuário", max_length=40)   
    email = forms.EmailField(label="Email", max_length=100)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)

class FormLogin(forms.Form):
    user = forms.CharField(label="Usuario", max_length=40)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)

class SalaForm(forms.ModelForm):
    class Meta:
        model = Salas
        fields = ['horario']  # Campos que você deseja permitir atualização
    
    
    def clean_horarios(self):
        horarios = self.cleaned_data.get('horarios')
        if horarios:
            for horario in horarios:
                horario_time = timezone.datetime.strptime(horario, "%H:%M").time()
                if not (timezone.datetime.strptime("07:05", "%H:%M").time() <= horario_time <= timezone.datetime.strptime("17:10", "%H:%M").time()):
                    raise forms.ValidationError("O horário de agendamento deve ser entre 7:05 e 17:10.")
        return horarios

class FormAgendamentosSala(forms.Form):
    data = forms.DateField(label="Data", widget=forms.DateInput(attrs={'type': 'date'}))
    descricao = forms.CharField(label="Descrição", max_length=100)
    equipamentos = forms.CharField(label="Equipamentos", max_length=100)
    sala = forms.ModelChoiceField(queryset=Salas.objects.all(), label="Sala")
    horarios = forms.MultipleChoiceField(
        label="Horários",
        choices=[(f"{h:02}:{m:02}", f"{h:02}:{m:02}") for h in range(7, 18) for m in (5, 10)],
        widget=forms.CheckboxSelectMultiple
    )

    def clean_horarios(self):
        horarios = self.cleaned_data.get('horarios')
        if horarios:
            for horario in horarios:
                horario_time = timezone.datetime.strptime(horario, "%H:%M").time()
                if not (timezone.datetime.strptime("07:05", "%H:%M").time() <= horario_time <= timezone.datetime.strptime("17:10", "%H:%M").time()):
                    raise forms.ValidationError("O horário de agendamento deve ser entre 7:05 e 17:10.")
        return horarios

class AdicionarSalaForm(forms.ModelForm):
    class Meta:
        model = Salas
        fields = ['salas', 'descricao', 'equipamentos']