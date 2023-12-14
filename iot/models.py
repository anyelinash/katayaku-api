from django.db import models
from users.models import Empresa, Usuario

#prueba
class Rele(models.Model):
    nombre = models.CharField(max_length=255)
    topico = models.CharField(max_length=255)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
###


# Módulos
class Modulo(models.Model):
    cod_modulo = models.AutoField(primary_key=True)
    codigo_usu = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)
    descripcion = models.TextField()
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre


# Relé
class RegistrosRele(models.Model):
    is_on = models.BooleanField(default=False)
    cod_registro = models.AutoField(primary_key=True)
    cod_modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    #accion = models.CharField(max_length=25)

    def __str__(self):
        return f'Registro de Relé {self.cod_registro}'


# Sensor de flujo de agua
class RegistrosAgua(models.Model):
    cod_registro = models.AutoField(primary_key=True)
    cod_modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    flujo = models.DecimalField(max_digits=10, decimal_places=2)
    unidadmedida = models.CharField(max_length=5)
    nivelflujo = models.CharField(max_length=25)

    def __str__(self):
        return f'Registro de Agua {self.cod_registro}'


# Sensor ultrasónico
class RegistrosUltrasonico(models.Model):
    cod_registro = models.AutoField(primary_key=True)
    cod_modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    distancia = models.DecimalField(max_digits=10, decimal_places=2)
    unidadmedida = models.CharField(max_length=255)
    detecmov = models.BooleanField()

    def __str__(self):
        return f'Registro Ultrasonico {self.cod_registro}'


# Sensor de calidad de aire
class RegistrosAire(models.Model):
    cod_registro = models.AutoField(primary_key=True)
    cod_modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    calidad_aire = models.CharField(max_length=255)
    monoxcarbono = models.DecimalField(max_digits=10, decimal_places=2)
    amoniaco = models.DecimalField(max_digits=10, decimal_places=2)
    alerta = models.CharField(max_length=255)
    dlargo_plazo = models.DecimalField(max_digits=10, decimal_places=2)
    cont_ventilacion = models.BooleanField()
    cot_purificado = models.BooleanField()

    def __str__(self):
        return f'Registro de Aire {self.cod_registro}'


# Alertas
class AlertasRele(models.Model):
    cod_alerta = models.AutoField(primary_key=True)
    cod_modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    cod_registro = models.ForeignKey(RegistrosRele, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    tipo_alerta = models.CharField(max_length=255)

    def __str__(self):
        return f'Alerta {self.cod_alerta}'

class AlertasAire(models.Model):
    cod_alerta = models.AutoField(primary_key=True)
    cod_modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    cod_registro = models.ForeignKey(RegistrosAire, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    tipo_alerta = models.CharField(max_length=255)

    def __str__(self):
        return f'Alerta {self.cod_alerta}'

# mantenimientos
class Mantenimientos(models.Model):
    cod_mant = models.AutoField(primary_key=True)
    codigo_emp = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    tipo_mant = models.CharField(max_length=255)
    descripcion = models.TextField()
    realizado = models.BooleanField()

    def __str__(self):
        return f'Mantenimiento {self.cod_mant}'


# temporizadores
class Temporizadores(models.Model):
    cod_temp = models.AutoField(primary_key=True)
    codigo_emp = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    temp_inicio = models.DateTimeField()
    temp_fin = models.DateTimeField()
    accion = models.CharField(max_length=25)

    def __str__(self):
        return f'Temporizador {self.cod_temp}'
