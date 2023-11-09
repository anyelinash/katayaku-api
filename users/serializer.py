from rest_framework import serializers
from .models import Empresa, Usuario

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('codigo_emp', 'nombre', 'ruc', 'correo', 'contrasena')

class UsuarioSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Usuario
        fields = ('codigo_usu', 'codigo_emp', 'nombre', 'dni', 'correo', 'contrasena')