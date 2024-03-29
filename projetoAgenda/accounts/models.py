from django.db import models
from index.models import Contato
from django import forms


class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ('mostrar', 'data_criacao')
