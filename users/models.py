from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Usuarios
class UsuarioManager(BaseUserManager):
    def create_user(self, correo, contrasena=None, **extra_fields):
        if not correo:
            raise ValueError('El correo electrónico es obligatorio')
        email = self.normalize_email(correo)
        user = self.model(correo=email, **extra_fields)
        user.set_password(contrasena)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, contrasena=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True')

        return self.create_user(correo, contrasena, **extra_fields)


class Usuario(AbstractBaseUser):
    codigo_usu = models.AutoField(primary_key=True)  # PK autoincremental
    provider_id = models.CharField(max_length=255)
    provider_specific_uid = models.CharField(max_length=255)
    nombre = models.CharField(max_length=200)
    dni = models.CharField(max_length=8)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    correo = models.EmailField(unique=True)
    password = models.CharField(max_length=128, default='')
    photo_url = models.URLField()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre', 'dni', 'telefono', 'correo','password']

    def __str__(self):
        return self.nombre

    def logout(self):
        # Puedes personalizar este método según tus necesidades
        # Por ejemplo, aquí podrías invalidar tokens de autenticación, si estás utilizando tokens.
        pass


# Empresa
class Empresa(models.Model):
    codigo_emp = models.AutoField(primary_key=True)  # PK autoincremental
    codigo_usu = models.ForeignKey(Usuario, on_delete=models.CASCADE) # FK a la tabla Usuario
    nombre = models.CharField(max_length=200)
    ruc = models.CharField(max_length=11)
    correo = models.EmailField()
    contrasena = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


# Reportes de usuario
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