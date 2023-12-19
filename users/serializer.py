from rest_framework import serializers
from .models import Empresa, Usuario, Reporte


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('codigo_emp', 'codigo_usu', 'nombre', 'ruc', 'correo', 'contrasena')


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['codigo_usu', 'provider_id', 'provider_specific_uid', 'nombre', 'dni', 'telefono', 'correo', 'photo_url']


class UsuarioRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['codigo_usu', 'provider_id', 'provider_specific_uid', 'nombre', 'dni', 'correo', 'password', 'photo_url']

    def create(self, validated_data):
        user = Usuario.objects.create_user(**validated_data)
        return user


class UsuarioLoginSerializer(serializers.Serializer):
    correo = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})


# Reportes de usuarios
class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'
