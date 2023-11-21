from rest_framework import serializers
from .models import Empresa, Usuario, Reporte


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('codigo_emp', 'codigo_usu', 'nombre', 'ruc', 'correo', 'contrasena')


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('codigo_usu', 'provider_id', 'provider_specific_uid','nombre', 'dni', 'correo', 'contrasena', 'photo_url')
        

# Reportes de usuarios
class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'
