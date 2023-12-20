from rest_framework import serializers
from .models import Empresa, Usuario, Reporte
from django.contrib.auth import authenticate
from rest_framework import serializers


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('codigo_emp', 'codigo_usu', 'nombre', 'ruc', 'correo', 'contrasena')


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class UsuarioRegistrationSerializer(serializers.ModelSerializer):
    contrasena = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['correo', 'contrasena', 'nombres', 'apellidos', 'dni', 'telefono', 'photo_url']

    def create(self, validated_data):
        return Usuario.objects.create_user(**validated_data)


class UsuarioLoginSerializer(serializers.Serializer):
    correo = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        correo = data.get('correo')
        password = data.get('contrasena')

        if not correo or not password:
            raise serializers.ValidationError('Correo y contraseña son requeridos')

        return data


# Reportes de usuarios
class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'
