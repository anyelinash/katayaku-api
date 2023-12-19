from rest_framework import serializers
from .models import Empresa, Usuario, Reporte


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
    contrasena = serializers.CharField(style={'input_type': 'password'})


# Reportes de usuarios
class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'
