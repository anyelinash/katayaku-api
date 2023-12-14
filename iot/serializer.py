from rest_framework import serializers
from .models import *


# prueba
class RelaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Rele
        fields = ['id', 'nombre', 'topico', 'status']


#

# Módulos - General
class ModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulo
        fields = ('cod_modulo', 'codigo_usu', 'nombre', 'ubicacion', 'descripcion', 'estado')


# Relé
class ReleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrosRele
        fields = ('is_on', 'cod_registro', 'cod_modulo', 'fecha_hora')

# Sensor de calidad de aire
class AireSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrosAire
        fields = '__all__'


# Alertas
# Alertas Rele
class AlertReleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertasRele
        fields = '__all__'

# Alertas Sensor de calidad de aire
class AlertAireSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertasAire
        fields = '__all__'


# mantenimientos
class MantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mantenimientos
        fields = '__all__'


# temporizadores
class TemporizadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temporizadores
        fields = '__all__'
