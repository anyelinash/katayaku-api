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

#Reportes de usuario
class Reporte(models.Model):
    LUZ = 'Reporte de Luz'
    AGUA = 'Reporte de Agua'
    AIRE = 'Reporte de Calidad de Aire'
    ULTRASONIC = 'Reporte de Movimiento'


    REPORTES_CHOICES = (
        (LUZ, 'Reporte de Luz'),
        (AGUA, 'Reporte de Agua'),
        (AIRE, 'Reporte de Calidad de Aire'),
        (ULTRASONIC, 'Reporte de Movimiento'),
    )
    codigo_emp = models.ForeignKey(Empresa, on_delete=models.CASCADE)  # FK a la tabla Empresa
    codigo_usu = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # FK a la tabla Empresa
    codigo_rep = models.AutoField(primary_key=True)  # PK autoincremental
    nombre_usu = models.CharField(max_length=200)
    tipo_rep = models.CharField(max_length=30, choices=REPORTES_CHOICES)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    descripcion = models.CharField(max_length=250)
