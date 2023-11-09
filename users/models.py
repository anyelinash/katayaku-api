from django.db import models

#Empresa
class Empresa(models.Model):
    codigo_emp = models.AutoField(primary_key=True)  # PK autoincremental
    nombre = models.CharField(max_length=200)
    ruc = models.CharField(max_length=11)
    correo = models.EmailField()
    contrasena = models.CharField(max_length=20) 

    def __str__(self):
        return self.nombre

#Usuarios
class Usuario(models.Model):
    codigo_usu = models.AutoField(primary_key=True)  # PK autoincremental
    codigo_emp = models.ForeignKey(Empresa, on_delete=models.CASCADE)  # FK a la tabla Empresa
    nombre = models.CharField(max_length=200)
    dni = models.CharField(max_length=8)
    correo = models.EmailField()
    contrasena = models.CharField(max_length=20)  

    def __str__(self):
        return self.nombre