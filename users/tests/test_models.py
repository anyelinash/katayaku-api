from django.test import TestCase
from django.contrib.auth import get_user_model
from users.models import Empresa, Reporte

User = get_user_model()


class UsuarioModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            correo='test@example.com',
            contrasena='testpassword',
            nombres='John',
            apellidos='Doe',
            dni='12345678',
            telefono='123456789',
            photo_url='https://example.com/photo.jpg',
        )

    def test_usuario_creation(self):
        self.assertEqual(self.user.usuario, 'John_Doe_test@example.com')

    def test_empresa_creation(self):
        empresa = Empresa.objects.create(
            codigo_usu=self.user,
            numero='123',
            nombre_o_razon_social='Empresa de Prueba',
            tipo_contribuyente='Contribuyente',
            estado='Activo',
            condicion='Regular',
            departamento='Lima',
            provincia='Lima',
            distrito='Miraflores',
            direccion='Av. Prueba 123',
            direccion_completa='Av. Prueba 123, Miraflores, Lima',
        )
        self.assertEqual(str(empresa), '123')

    def test_reporte_creation(self):
        empresa = Empresa.objects.create(
            codigo_usu=self.user,
            numero='123',
            nombre_o_razon_social='Empresa de Prueba',
            tipo_contribuyente='Contribuyente',
            estado='Activo',
            condicion='Regular',
            departamento='Lima',
            provincia='Lima',
            distrito='Miraflores',
            direccion='Av. Prueba 123',
            direccion_completa='Av. Prueba 123, Miraflores, Lima',
        )
        reporte = Reporte.objects.create(
            codigo_emp=empresa,
            codigo_usu=self.user,
            nombre_usu='John Doe',
            tipo_rep=Reporte.LUZ,
            descripcion='Informe de prueba de luz',
        )
        self.assertEqual(str(reporte), str(reporte.codigo_rep))


# Puedes agregar más pruebas según sea necesario.
