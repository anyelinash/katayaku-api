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
        fields = ('cod_modulo', 'codigo_emp', 'nombre', 'ubicacion', 'descripcion', 'estado')


# Relé
class ReleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrosRele
        fields = ('is_on', 'cod_registro', 'cod_modulo', 'fecha_hora')


# Sensor de flujo de agua
class AguaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrosAgua
        fields = ('cod_registro', 'cod_modulo', 'fecha_hora', 'flujo', 'unidadmedida', 'nivelflujo')


# Sensor ultrasónico
class SonicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrosUltrasonico
        fields = '__all__'


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


# Alertas Sensor de flujo de agua
class AlertAguaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertasAgua
        fields = '__all__'


# Alertas Sensor ultrasónico
class AlertSonicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertasSonico
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
