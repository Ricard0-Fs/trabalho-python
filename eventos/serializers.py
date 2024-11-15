from rest_framework import serializers
from .models import Evento, Participante

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['id', 'nome', 'data', 'local', 'participantes']
        depth = 1

class ParticipanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = ['id', 'nome', 'email', 'evento']
