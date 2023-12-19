from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UsuarioManager(BaseUserManager):
    def create_user(self, correo, contrasena=None, **extra_fields):
        if not correo:
            raise ValueError('El correo electrónico es obligatorio')
        email = self.normalize_email(correo)
        user = self.model(email=email, **extra_fields)
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


class Usuario(AbstractBaseUser, PermissionsMixin):
    codigo_usu = models.AutoField(primary_key=True)
    provider_id = models.CharField(max_length=255)
    provider_specific_uid = models.CharField(max_length=255)
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    dni = models.CharField(max_length=8)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    correo = models.EmailField(unique=True)
    photo_url = models.URLField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'correo'

    # No es necesario definir el campo 'password' aquí, ya que está incluido en AbstractBaseUser

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.correo}"

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='usuario_groups',  # Cambia 'usuario_groups' a algo único y significativo
        help_text='The groups this user belongs to.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='usuario_user_permissions',  # Cambia 'usuario_user_permissions' a algo único y significativo
        help_text='Specific permissions for this user.',
    )




# Empresa
class Empresa(models.Model):
    objects = None
    codigo_emp = models.AutoField(primary_key=True)  # PK autoincremental
    codigo_usu = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # FK a la tabla Usuario
    numero = models.CharField(max_length=20, default='')
    nombre_o_razon_social = models.CharField(max_length=255, default='')
    tipo_contribuyente = models.CharField(max_length=50, default='')
    estado = models.CharField(max_length=20, default='')
    condicion = models.CharField(max_length=20, default='')
    departamento = models.CharField(max_length=50, default='')
    provincia = models.CharField(max_length=50, default='')
    distrito = models.CharField(max_length=50, default='')
    direccion = models.CharField(max_length=255, default='')
    direccion_completa = models.CharField(max_length=255, default='')

    def _str_(self):
        return self.numero


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
